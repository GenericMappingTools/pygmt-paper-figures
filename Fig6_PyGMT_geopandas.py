import geopandas as gpd
import pygmt

provider = "https://naciscdn.org/naturalearth"
states = gpd.read_file(f"{provider}/110m/cultural/ne_110m_admin_1_states_provinces.zip")
states["area_sqkm"] = states.geometry.to_crs(epsg=6933).area / 10 ** 9
states = states[states["name"] != "Alaska"]
rivers = gpd.read_file(f"{provider}/110m/physical/ne_110m_rivers_lake_centerlines.zip")
rivers = rivers.cx[-126:-66, 24.9:49.1]
cities = gpd.read_file(f"{provider}/110m/cultural/ne_110m_populated_places_simple.zip")
cities = cities.cx[-126:-66, 25.7:42]

fig = pygmt.Figure()
fig.basemap(projection="L-96/35/33/41/12c", region=[-126, -66, 25, 49], frame="+n")

pygmt.makecpt(cmap="bilbao", series=[0, states["area_sqkm"].max()])
fig.plot(data=states, cmap=True, pen="0.2p,gray50", fill="+z", aspatial="Z=area_sqkm")
fig.colorbar(frame="xaf+lArea (1000 km@+2@+)", position="jBL+h+o1.4c/0.6c+w3.5c+ml")

fig.plot(data=rivers, pen="0.5p,dodgerblue4")

fig.plot(data=cities, style="s0.17c", fill="darkorange", pen="0.5p")
fig.text(
    x=cities.geometry.x,
    y=cities.geometry.y,
    text=cities["name"],
    offset="0.35c/0.2c",
    justify="BC",
    font="4.5p,Helvetica-Bold",
    fill="white@30",
    pen="0.2p,darkorange",
    clearance="0.05c+tO",
)

fig.show()
fig.savefig(fname="Fig6_PyGMT_geopandas_usa.png")


# %%
import geodatasets
import geopandas as gpd
import pygmt
from pygmt.params import Box

chicago = gpd.read_file(geodatasets.get_path("geoda airbnb"))

provider = "https://naciscdn.org/naturalearth"
railroads = gpd.read_file(f"{provider}/10m/cultural/ne_10m_railroads.zip")
airports = gpd.read_file(f"{provider}/10m/cultural/ne_10m_airports.zip")
cities = gpd.read_file(f"{provider}/10m/cultural/ne_10m_populated_places_simple.zip")
ports = gpd.read_file(f"{provider}/10m/cultural/ne_10m_ports.zip")
railroads = railroads.cx[-87.94:-87.52, 41.64:42.02]
airports = airports.cx[-87.94:-87.52, 41.64:42.02]
cities = cities.cx[-87.94:-87.52, 41.64:42.02]
ports = ports.cx[-87.94:-87.52, 41.64:42.02]

fig = pygmt.Figure()
fig.basemap(region=chicago.total_bounds[[0, 2, 1, 3]], projection="M10c", frame="+n")
fig.coast(shorelines=True, lakes="lightblue", land="gray95")

pygmt.makecpt(cmap="bilbao", series=[0, chicago["population"].max()])

fig.plot(data=chicago, pen="0.5p,gray30", fill="+z", cmap=True, aspatial="Z=population")

fig.plot(data=railroads["geometry"], pen="2p,black")
fig.plot(data=railroads["geometry"], pen="1p,white,2_2")

fig.plot(data=cities["geometry"], style="s0.32c", fill="red", pen="1p", label="city")
fig.plot(data=ports["geometry"], style="i0.35c", fill="steelblue", pen="1p", label="harbor")
fig.plot(data=airports["geometry"], style="t0.35c", fill="darkorange", pen="1p", label="airport")
fig.text(
    x=airports.geometry.x,
    y=airports.geometry.y,
    text=airports["name"],
    offset="-0.25c",
    justify="TL",
    font="8p,Helvetica-Bold",
    fill="white@30",
    pen="0.8p,darkorange",
    clearance="0.08c+tO",
)

fig.colorbar(
    frame="xaf+lPopulation in Chicago",
    position="jML+o0.95c/-1.5c+w7c+ml",
    box=Box(fill="gray95", clearance="0.5c"),
)
fig.legend(position="jTR+o0.2c+l1.7", box=Box(fill="white@30", pen="0.5p,gray50"))

fig.show()
fig.savefig(fname="Fig6_PyGMT_geopandas_chicago.png")


# %%
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

fig.plot(data=rivers, pen="1.5p,dodgerblue4")

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
fig.savefig(fname="Fig6_PyGMT_geopandas_africa.png")