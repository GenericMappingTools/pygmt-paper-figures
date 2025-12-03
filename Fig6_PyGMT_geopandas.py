import geopandas as gpd
import pygmt

provider = "https://naciscdn.org/naturalearth"
states = gpd.read_file(f"{provider}/50m/cultural/ne_50m_admin_1_states_provinces.zip")
rivers = gpd.read_file(f"{provider}/50m/physical/ne_50m_rivers_lake_centerlines.zip")
cities = gpd.read_file(f"{provider}/110m/cultural/ne_110m_populated_places_simple.zip")

states = states[states["admin"] == "United States of America"]
rivers = rivers[rivers.intersects(states.union_all())]
cities = cities[cities["adm0name"] == "United States of America"]

states["area"] = states.to_crs(epsg=6933).area / 10 ** 9

fig = pygmt.Figure()
fig.basemap(projection="L-96/35/33/41/12c", region=[-126, -66, 25, 49], frame="+n")

pygmt.makecpt(cmap="hawaii", series=[0, states["area"].max()], reverse=True)
fig.plot(data=states, cmap=True, pen="0.2p,gray50", fill="+z", aspatial="Z=area")
fig.colorbar(frame="xaf+lArea (1000 km@+2@+)", position="jRB+o1.9c/0.2c+w3c/0.15c+ml")

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

# Add the states Alaska and Hawaii separately in the lower left corner
for name, xshift in zip(["Alaska", "Hawaii"], ["1.2c", "2.8c"]):
    substate = states[(states["name"] == name)]
    substate = substate.explode()
    substate = substate[substate.to_crs(epsg=6933).area > 1.0e8].dissolve()
    region = pygmt.info(substate, spacing=1)
    with fig.shift_origin(xshift=xshift):
        fig.plot(
            data=substate,
            region=region,
            projection="M2c",
            cmap=True,
            pen="0.2p,gray50",
            fill="+z",
            aspatial="Z=area",
        )

fig.show()
fig.savefig(fname="Fig6_PyGMT_geopandas.png")
