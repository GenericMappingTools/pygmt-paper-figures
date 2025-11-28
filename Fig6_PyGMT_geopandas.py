import geopandas as gpd
import pygmt

provider = "https://naciscdn.org/naturalearth"
world = gpd.read_file(f"{provider}/110m/cultural/ne_110m_admin_0_countries.zip")
world["POP_EST"] *= 1e-6
africa = world[world["CONTINENT"] == "Africa"].copy()
rivers = gpd.read_file(f"{provider}/110m/physical/ne_110m_rivers_lake_centerlines.zip")
cities = gpd.read_file(f"{provider}/110m/cultural/ne_110m_populated_places_simple.zip")
cities_africa = gpd.sjoin(cities, africa, how="inner")
cities_large = cities_africa[cities_africa["worldcity"] == 1].copy()
cities_small = cities_africa[cities_africa["worldcity"] != 1].copy()

fig = pygmt.Figure()
fig.basemap(region=[-19.5, 52, -37, 38], projection="M15c", frame="+n")

pygmt.makecpt(cmap="bilbao", series=(0, 200))
fig.plot(data=africa, pen="0.8p,gray50", fill="+z", cmap=True, aspatial="Z=POP_EST")
fig.colorbar(frame="x20f10+lPopulation (millions)", position="jML+o3c/-3.5c+w7.5c+ml")

fig.plot(data=rivers["geometry"], pen="1.5p,dodgerblue4")

fig.plot(data=cities_small, style="s0.2c", fill="lightgray", pen="1p")
fig.plot(data=cities_large, style="s0.3c", fill="darkorange", pen="1p")
fig.text(
    x=cities_large.geometry.x,
    y=cities_large.geometry.y,
    text=cities_large["name"],
    offset="0.2c/0.35c",
    justify="BL",
    font="10p,Helvetica-Bold",
    fill="white@30",
    pen="0.8p,darkorange",
    clearance="0.1c+tO",
)

fig.show()
fig.savefig(fname="Fig6_PyGMT_geopandas.png")
