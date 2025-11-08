import pygmt

region = [-25, -13, 63.2, 66.7]

fig = pygmt.Figure()
with fig.subplot(
    nrows=2,
    ncols=2,
    subsize=("12c", "8.5c"),
    autolabel="(a)+o0.1c/0.25c+gwhite@30",
    margins=("1.5c", "0.2c"),
    sharex="b",
    sharey="l",
    frame="WSrt",
):

    # Top left
    fig.basemap(region=region, projection="M?", panel=0)
    fig.coast(land="lightgray", water="lightblue", shorelines="1/0.5p,gray30")
    with pygmt.config(MAP_SCALE_HEIGHT="10p"):
        fig.basemap(map_scale="n0.86/0.1+c+w100k+f+l")

    # Top right
    fig.basemap(region=region, projection="M?", panel=1)
    grid_relief = pygmt.datasets.load_earth_relief(resolution="03m", region=region)
    fig.grdimage(grid=grid_relief, cmap="SCM/oleron")
    fig.colorbar(frame=["x+lsurface elevation", "y+lm"], position="JLM")
    fig.coast(shorelines="1/0.5p,gray30")

    # Bottom left
    fig.basemap(region=region, projection="M?", panel=2)
    grid_geoid = pygmt.datasets.load_earth_geoid(resolution="03m", region=region)
    fig.grdimage(grid=grid_geoid, cmap="SCM/lajolla")
    fig.grdcontour(grid=grid_geoid)
    fig.colorbar(frame=["x+lheight", "y+lm"], position="JRM")
    fig.coast(shorelines="1/0.5p,white")

    # Bottom right
    fig.tilemap(region=region, projection="M?", zoom=7, panel=3)

fig.show()
