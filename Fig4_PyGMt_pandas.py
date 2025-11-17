import io

import pygmt
import pandas as pd
import requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "csv",
    "starttime": "2010-01-01",
    "endtime": "2024-01-02",
    "minlatitude": 33,
    "maxlatitude": 53,
    "minlongitude": 131,
    "maxlongitude": 152,
    "minmagnitude": 4,
    "maxmagnitude": 6.5,
}
r = requests.get(url, params=params)
df_eqs = pd.read_csv(io.StringIO(r.text))
df_eqs = df_eqs.sort_values(by=["mag"], ascending=False)

fig = pygmt.Figure()

fig.basemap(region=[131, 152, 33, 51], projection="M15c", frame=True)
fig.coast(land="gray95", shorelines="gray50")

# Plot epicenters with color (hypocentral depth) or size (moment magnitude)
pygmt.makecpt(cmap="SCM/navia", series=[0, 500], reverse=True)
fig.colorbar(frame=["xa100f20+lHypocentral depth", "y+lkm"], position="+ef0.3c")
fig.plot(
    x=df_eqs.longitude,
    y=df_eqs.latitude,
    size=0.01 * 2**df_eqs.mag,
    fill=df_eqs.depth,
    cmap=True,
    style="c",
    pen="gray10",
)

# Add legend for size-coding
legend = io.StringIO(
    "\n".join(f"S 0.4 c {0.01 * 2**m:.2f} - 1p 1 Mw {m}" for m in [4, 5, 6])
)
fig.legend(spec=legend, position="jBR+o0.2c/0.5c+l2", box=True)

with fig.inset(
    position="jTL+w6c/3.5c+o0.1c",
    margin=(1.4, 0.2, 1, 0.2),
    box=pygmt.params.Box(fill="bisque"),
):
    fig.histogram(
        region=[3.9, 6.6, 0, 0],
        projection="X?/?",
        frame=["WSrt", "xa1af0.1+lMw", "yaf+lCounts"],
        data=df_eqs.mag,
        series=0.1,
        fill="darkgray",
        pen="lightgray",
        histtype=0,
    )

fig.show()
fig.savefig("Fig4_PyGMT_pandas.png")
