import geopandas as gpd
import pygmt

fig = pygmt.Figure()

fig.basemap(region=[-88, -87.5, 41.64, 42.04], projection="M9c", frame="rtlb")

gdf_airbnb = gpd.read_file("https://geodacenter.github.io/data-and-lab//data/airbnb.zip")
popul_min = gdf_airbnb["population"].min()
popul_max = gdf_airbnb["population"].max()

pygmt.makecpt(cmap="SCM/bilbao", series=[popul_min, popul_max, 10])
fig.colorbar(frame="x+lpopulation", position="jBL+jBL+o0.5c/0c+v")
fig.plot(
    data=gdf_airbnb,
    pen="0.2p,gray10",
    fill="+z",
    cmap=True,
    aspatial="Z=population",
)

fig.show()
fig.savefig(fname="Fig7_PyGMT_geopandas.png")
