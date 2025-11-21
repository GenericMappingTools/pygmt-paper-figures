import pygmt
from pygmt.datasets import load_mars_relief

mars = load_mars_relief(resolution="10m")
with pygmt.config(PROJ_ELLIPSOID="mars"):
    mars_filtered = mars.gmt.filter(filter="g50", distance=4)
    mars_gradient = mars_filtered.gmt.gradient(azimuth=-45, normalize="t1")

fig = pygmt.Figure()
pygmt.makecpt(cmap="batlow", series=[-6500, 6500])
fig.grdimage(
    mars_filtered,
    cmap=True,
    shading=mars_gradient,
    projection="G90/-20/12c",
    frame="g30",
)
fig.shift_origin(xshift="w+0.5c")
fig.grdimage(
    mars_filtered,
    cmap=True,
    shading=mars_gradient,
    projection="G270/20/12c",
    frame="g30",
)

fig.colorbar(
    frame=["xa2000f1000+lElevation of Mars", "y+lm"], position="+e0.3c+o-7c/1c"
)

fig.show()
fig.savefig(fname="Fig5_PyGMT_xarray_mars.png")
