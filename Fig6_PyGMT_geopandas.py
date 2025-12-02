import geopandas as gpd
import pygmt

provider = "https://naciscdn.org/naturalearth"
states = gpd.read_file(f"{provider}/50m/cultural/ne_50m_admin_1_states_provinces.zip")
rivers = gpd.read_file(f"{provider}/50m/physical/ne_50m_rivers_lake_centerlines.zip")
cities = gpd.read_file(f"{provider}/110m/cultural/ne_110m_populated_places_simple.zip")

states = states[states["admin"] == "United States of America"].copy()
states["area_sqkm"] = states.geometry.to_crs(epsg=6933).area / 10 ** 9
rivers = rivers[rivers.intersects(states.union_all())].copy()
cities = cities[cities["adm0name"] == "United States of America"].copy()

fig = pygmt.Figure()
fig.basemap(projection="L-96/35/33/41/12c", region=[-126, -66, 25, 49], frame="+n")

pygmt.makecpt(cmap="bilbao", series=[0, states["area_sqkm"].max()])
fig.plot(data=states, cmap=True, pen="0.2p,gray50", fill="+z", aspatial="Z=area_sqkm")
fig.colorbar(frame="xaf+lArea (1000 km@+2@+)", position="jRB+o1.9c/0.3c+w2.8c/0.12c+ml")

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

# Add Alaska and Hawaii separately
for xshift, region in zip(["0.9c", "2.3c"], [[172, 230, 51, 72], [-168, -154, 18, 29]]):
    with fig.shift_origin(xshift=xshift):
        fig.plot(
            data=states,
            region=region,
            projection="M2.5c",
            cmap=True,
            pen="0.2p,gray50",
            fill="+z",
            aspatial="Z=area_sqkm"
        )

fig.show()
fig.savefig(fname="Fig6_PyGMT_geopandas.png")
