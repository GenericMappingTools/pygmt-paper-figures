import io

import pygmt
import pandas as pd
import requests

url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "csv",
    "starttime": "2000-01-01",
    "endtime": "2025-10-30",
    "mindepth": 70,
    "minlatitude": 30, #33,
    "maxlatitude": 60, #53,
    "minlongitude": 120, #131,
    "maxlongitude": 168, #152,
    "minmagnitude": 5,
    # "maxmagnitude": 6.5,
    "orderby": "magnitude",
    "format": "csv",
}
r = requests.get(url, params=params)
df_eqs = pd.read_csv(io.StringIO(r.text))
df_eqs = df_eqs[df_eqs["magType"] != "mb"]  # Focus on moment magnitudes


fig = pygmt.Figure()
fig.basemap(region=[120, 168, 30, 60], projection="M15c", frame=True)
fig.coast(land="gray95", shorelines="gray50")

# Plot epicenters with color (hypocentral depth) or size (moment magnitude)
pygmt.makecpt(cmap="SCM/navia", series=[70, 700], reverse=True, transparency=30)
fig.colorbar(frame=["xa100f20+lHypocentral depth", "y+lkm"], position="+ef0.3c")
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
    "\n".join(f"S 0.4 c {0.005 * 2**m:.2f} - 1p 1 Mw {m}" for m in [5, 6, 7])
)
fig.legend(spec=legend, position="jBR+o0.2c+l2", box=True)

# Add histogramm for moment magnitude distribution
with fig.inset(
    position="jTL+w6c/3.5c+o0.1c",
    margin=(1.4, 0.2, 1, 0.2),
    box=pygmt.params.Box(fill="bisque"),
):
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
fig.savefig("Fig4_PyGMT_pandas_japan.png")



# %%
import io

import pygmt
import pandas as pd
import requests

lon_min = 75
lon_max = 110
lat_min = 0
lat_max = 30

lon_min = -90
lon_max = -30
lat_min = -50
lat_max = 10

hd_min = 70
mag_min = 5
mag_max = 6.5
start_time = "2000-01-01"
end_time = "2025-10-30"
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "csv",
    "starttime": start_time,
    "endtime": end_time,
    "mindepth": hd_min,
    # "minlatitude": lat_min,
    # "maxlatitude": lat_max,
    # "minlongitude": lon_min,
    # "maxlongitude": lon_max,
    "minmagnitude": mag_min,
    # "maxmagnitude": mag_max,
    "orderby": "magnitude",
}
r = requests.get(url, params=params)
df_eqs = pd.read_csv(io.StringIO(r.text))
df_eqs = df_eqs[df_eqs["magType"] != "mb"]  # Focus on moment magnitudes

fig = pygmt.Figure()
fig.basemap(region=[lon_min, lon_max, lat_min, lat_max], projection="M15c", frame=True)
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
    "\n".join(f"S 0.4 c {0.005 * 2**m:.2f} - 1p 1 Mw {m}" for m in [5, 6, 7])
)
fig.legend(spec=legend, position="jBR+o0.2c+l2", box=True)

# Add histogramm for moment magnitude distribution
with fig.inset(
    position="jRT+w5.5c/3.5c+o0.1c",
    margin=(1.3, 0.2, 1, 0.2),
    box=pygmt.params.Box(fill="bisque"),
):
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
fig.savefig("Fig4_PyGMT_pandas_myanmar.png")
