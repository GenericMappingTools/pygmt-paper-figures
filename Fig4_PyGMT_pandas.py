import io

import pygmt
import pandas as pd
import requests
from pygmt.params import Box

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "csv",
    "starttime": "2000-01-01",
    "endtime": "2025-10-30",
    "mindepth": 70,
    "minlongitude": 91,
    "maxlongitude": 134,
    "minlatitude": -21,
    "maxlatitude": 19,
    "minmagnitude": 5,
    "orderby": "magnitude",
}
r = requests.get(url, params=params)
df_eqs = pd.read_csv(io.StringIO(r.text))
df_eqs = df_eqs[df_eqs["magType"] != "mb"]  # Focus on moment magnitudes

fig = pygmt.Figure()
fig.basemap(region=[91, 134, -21, 19], projection="M15c", frame=True)
fig.coast(land="gray95", shorelines="gray50")

# Plot epicenters with color (hypocentral depth) or size (moment magnitude)
pygmt.makecpt(cmap="SCM/navia", series=[70, 700], reverse=True, transparency=30)
fig.colorbar(frame=["xaf+lHypocentral depth", "y+lkm"], position="+ef0.3c")
fig.plot(
    x=df_eqs.longitude,
    y=df_eqs.latitude,
    size=0.005 * 2**df_eqs.mag,
    fill=df_eqs.depth,
    cmap=True,
    style="c",
    pen="gray10",
)
# Add legend for size-coding
legend = io.StringIO(
    "\n".join(f"S 0.4 c {0.005 * 2**mag:.2f} - 1p 1 Mw {mag}" for mag in [5, 6, 7])
)
fig.legend(spec=legend, position="jBR+o0.2c+l2", box=Box(fill="white", pen="0.1p"))

# Add histogram for moment magnitude distribution
with fig.inset(
    position="jBL+w7c/4c+o0.1c", margin=(1.1, 0.2, 0.9, 0.2), box=Box(fill="bisque")
):
    with pygmt.config(FONT="8p"):
        fig.histogram(
            region=[4.8, 10.2, 0, 0],
            projection="X?/?",
            frame=["WSrt", "xa1f0.2+lMw", "yaf+lCounts"],
            data=df_eqs.mag,
            series=0.2,
            fill="darkgray",
            pen="lightgray",
            histtype=0,
        )

fig.show()
fig.savefig("Fig4_PyGMT_pandas.png")
