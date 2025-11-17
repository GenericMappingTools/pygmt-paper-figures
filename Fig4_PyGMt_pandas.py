import io

import pygmt
import pandas as pd

# TODO request data
df_eqs = pygmt.datasets.load_sample_data(name="japan_quakes")

fig = pygmt.Figure()

fig.basemap(region=[131, 152, 33, 51], projection="M15c", frame=True)
fig.coast(land="gray95", shorelines="gray50")

# Plot epicenters with color (hypocentral depth) or size (moment magnitude)
pygmt.makecpt(cmap="SCM/navia", series=[0, 500], reverse=True)
fig.colorbar(frame=["xa100f20+lHypocentral depth", "y+lkm"], position="+ef0.3c")
fig.plot(
    x=df_eqs.longitude,
    y=df_eqs.latitude,
    size=0.02 * 2**df_eqs.magnitude,
    fill=df_eqs.depth_km,
    cmap=True,
    style="c",
    pen="gray10",
)

# Add legend for size-coding
legend = io.StringIO(
    "\n".join(f"S 0.4 c {0.02 * 2**m:.2f} - 1p 1 Mw {m}" for m in [3, 4, 5])
)
fig.legend(spec=legend, position="jBR+o0.2c+l2", box=True)

with fig.inset(
    position="jTL+w5.5/3.5c+o0.1c",
    margin=(1, 0.2, 1, 0.2),
    box=pygmt.params.Box(fill="bisque"),
):
    fig.histogram(
        region=[3.9, 7.1, 0, 0],
        projection="X?/?",
        frame=["WSrt", "xa1af0.1+lMw", "yaf+lCounts"],
        data=df_eqs.magnitude,
        series=0.1,
        fill="darkgray",
        pen="lightgray",
        histtype=0,
    )

fig.show()
fig.savefig("Fig4_PyGMT_pandas.png")
