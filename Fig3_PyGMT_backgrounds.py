import pygmt

region = [-25, -13, 63.2, 66.7]

fig = pygmt.Figure()
with fig.subplot(
    nrows=2,
    ncols=2,
    subsize=("12c", "8.5c"),
    autolabel="(a)+o0.15c/0.3c+gwhite@30+v",
    margins=("0.3c", "0.2c"),
    sharex="b",
    sharey="l",
    frame="WSrt",
):

    # Top left
    fig.basemap(region=region, projection="M?", panel=0)
    fig.coast(land="gray", water="lightblue", shorelines=True, resolution="high")
    fig.basemap(map_scale="n0.86/0.1+c+w100k+f+l")

    # Bottom left
    fig.tilemap(region=region, projection="M?", zoom=7, panel=1)

    # Top right
    grd_relief = pygmt.datasets.load_earth_relief(resolution="01m", region=region)
    fig.basemap(region=region, projection="M?", panel=2)
    fig.grdimage(grid=grd_relief, cmap="SCM/oleron", shading=True)
    fig.colorbar(frame=["xa500f250+lElevation", "y+lm"], position="JRM", shading=True)

    # Bottom right
    fig.basemap(region=region, projection="M?", perspective=(-150, 25), panel=3)
    fig.grdview(
        grid=grd_relief,
        cmap="SCM/oleron",
        surftype="s",
        shading=True,
        zsize="1.5c",
        plane="+ggrey",
        perspective=True,
    )

fig.show()
fig.savefig("Fig3_PyGMT_backgrounds.png")
