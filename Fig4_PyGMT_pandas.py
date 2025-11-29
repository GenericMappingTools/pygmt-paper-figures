import io

import pandas as pd
import pygmt
import requests
from pygmt.params import Box

params = {
    "format": "csv",
    "starttime": "2000-01-01",
    "endtime": "2025-10-30",
    "mindepth": 70,
    "minmagnitude": 5,
}
r = requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query", params=params)
df_eqs = pd.read_csv(io.StringIO(r.text))
df_eqs = df_eqs[
    (df_eqs["longitude"] >= 91)
    & (df_eqs["longitude"] <= 134)
    & (df_eqs["latitude"] >= -22)
    & (df_eqs["latitude"] <= 19)
].sort_values(by="mag", ascending=False)

fig = pygmt.Figure()
fig.basemap(region=[91, 134, -22, 19], projection="M15c", frame=True)
fig.coast(land="gray95", shorelines="gray50")

# Plot epicenters with color (hypocentral depth) or size (magnitude)
pygmt.makecpt(cmap="SCM/navia", series=[0, 700], reverse=True, transparency=30)
fig.plot(
    x=df_eqs.longitude,
    y=df_eqs.latitude,
    style="c",
    size=0.005 * 2**df_eqs.mag,
    fill=df_eqs.depth,
    cmap=True,
    pen="gray10",
)
fig.colorbar(frame=["xaf+lHypocentral depth", "y+lkm"])
# Add legend for size-coding
legend = io.StringIO(
    "\n".join(f"S 0.4 c {0.005 * 2**mag:.2f} - 1p 1 M {mag}" for mag in [5, 6, 7])
)
fig.legend(spec=legend, position="jBR+o0.2c+l2", box=Box(fill="white", pen="black"))

# Add histogram for magnitude distribution
with fig.inset(position="jBL+w7c/4c+o0.2c", margin=(1.2, 0.2, 0.9, 0.2), box=True):
    with pygmt.config(FONT="8p"):
        fig.histogram(
            region=[4.8, 10.2, 0, 0],
            projection="X?/?",
            frame=["WSrt", "xa1f0.2+lM", "yaf+lCounts"],
            data=df_eqs.mag,
            series=0.2,
            fill="darkgray",
            pen="lightgray",
            histtype=0,
        )

fig.show()
fig.savefig("Fig4_PyGMT_pandas.png")
