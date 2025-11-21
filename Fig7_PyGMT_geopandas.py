import pygmt
import geopandas as gpd

world = gpd.read_file("https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip")
rivers = gpd.read_file("https://naciscdn.org/naturalearth/110m/physical/ne_110m_rivers_lake_centerlines.zip")
cities = gpd.read_file("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_populated_places_simple.zip")
cities_mega = cities[cities["megacity"]==1]  # Focus on large cities
cities_world = cities[cities["worldcity"]==1]
world["POP_EST"] *= 1e-6

for region, label in zip(
    [[-89, -33, -56.5, 10], [-13, 27, 33, 67], [-19.5, 53, -38, 37.5]],
    ["region1", "region2", "region3"],
):

    fig = pygmt.Figure()
    fig.basemap(region=region, projection="M15c", frame=True)
    pygmt.makecpt(cmap="bilbao", series=(0, 270, 10))
    fig.plot(
        data=world[["POP_EST", "geometry"]],
        pen="1p,gray50",
        fill="+z",
        cmap=True,
        aspatial="Z=POP_EST",
    )
    fig.colorbar(frame="x+lPopulation (millions)")
    fig.plot(data=rivers["geometry"], pen="1.5p,darkblue")
    fig.plot(data=cities["geometry"], style="s0.25c", fill="red", pen="1p,black")
    fig.text(
        x=cities_world.geometry.x,
        y=cities_world.geometry.y,
        text=cities_world["name"],
        font="10p,Helvetica-Bold,black",
        offset="0c/-0.25c",
        justify="TR",
        fill="white@30",
    )
    fig.show()
    fig.savefig(fname=f"Fig7_PyGMT_geopandas_{label}.png")
