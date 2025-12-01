import pygmt
from pygmt.datasets import load_mars_relief

mars = load_mars_relief(resolution="10m")
with pygmt.config(PROJ_ELLIPSOID="mars"):
    mars_filter = mars.gmt.filter(filter="g50", distance=4)
    mars_grad = mars_filter.gmt.gradient(azimuth=-45, normalize="t1")

fig = pygmt.Figure()
pygmt.makecpt(cmap="batlow", series=[-6500, 6500])
fig.grdimage(
    mars_filter, cmap=True, shading=mars_grad, projection="G270/20/12c", frame="g30",
)
fig.shift_origin(xshift="w+0.5c")
fig.grdimage(
    mars_filter, cmap=True, shading=mars_grad, projection="G90/-20/12c", frame="g30",
)
fig.colorbar(
    frame=["xa2000f1000+lElevation", "y+lm"], position="+e0.3c+o-6.25c/0.2c+ml"
)
fig.show()
fig.savefig(fname="Fig5_PyGMT_xarray.png")
