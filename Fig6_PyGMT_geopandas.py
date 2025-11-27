import geopandas as gpd
import pygmt

provider = "https://naciscdn.org/naturalearth"
world = gpd.read_file(f"{provider}/50m/cultural/ne_50m_admin_0_countries.zip")
world["POP_EST"] *= 1e-6
rivers = gpd.read_file(f"{provider}/110m/physical/ne_110m_rivers_lake_centerlines.zip")
cities = gpd.read_file(f"{provider}/110m/cultural/ne_110m_populated_places_simple.zip")
cities_small = cities[cities["worldcity"] != 1].copy()  # Smaller cities
cities_world = cities[cities["worldcity"] == 1].copy()  # Larger (world) cities

fig = pygmt.Figure()
fig.basemap(region=[-19.5, 53, -38, 37.5], projection="M15c", frame=True)

pygmt.makecpt(cmap="bilbao", series=(0, 200))
fig.plot(data=world, pen="1p,gray50", fill="+z", cmap=True, aspatial="Z=POP_EST")
fig.colorbar(frame="x10f5+lPopulation (millions)")

fig.plot(data=rivers, pen="1.5p,darkblue")

fig.plot(data=cities_small, style="s0.2c", fill="lightgray", pen="1p")
fig.plot(data=cities_world, style="s0.3c", fill="darkorange", pen="1p")
fig.text(
    x=cities_world.geometry.x,
    y=cities_world.geometry.y,
    text=cities_world["name"],
    offset="0c/-0.3c",
    justify="TR",
    font="10p,Helvetica-Bold",
    fill="white@50",
    pen="0.8p,darkorange",
    clearance="0.1c+tO",
)

fig.show()
fig.savefig(fname="Fig6_PyGMT_geopandas.png")
