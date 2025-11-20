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


# %%
import pygmt
import geopandas as gpd

region = "=SA"
region = [-89, -33, -56.5, 9.7]

world = gpd.read_file("https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip")
rivers = gpd.read_file("https://naciscdn.org/naturalearth/110m/physical/ne_110m_rivers_lake_centerlines.zip")
cities = gpd.read_file("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_populated_places_simple.zip")

world["POP_EST"] *= 1.0e-5

fig = pygmt.Figure()
fig.basemap(region=region, projection="M15c", frame=True)
pygmt.makecpt(cmap="batlow", series=(0, 2700, 100)) # 30000
fig.plot(
    data=world[["POP_EST", "geometry"]],
    pen="1p,gray50",
    fill="+z",
    cmap=True,
    aspatial="Z=POP_EST",
)
fig.colorbar(frame=["x+lPopulation", "y+l*10e-5"])
fig.plot(data=rivers["geometry"], pen="1.5p,skyblue")
fig.plot(data=cities["geometry"], style="s0.3c", fill="red", pen="1p,black")
fig.text(
    x=cities.geometry.x,
    y=cities.geometry.y,
    text=cities["name"],
    font="10p,Helvetica-Bold,black",
    offset="0c/-0.3c",
    justify="TR",
    fill="white@30",
)
fig.show()
fig.savefig(fname="Fig7_PyGMT_geopandas_ne.png")
