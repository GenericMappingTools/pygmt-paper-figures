# import pygmt
# import xarray as xr

# url = "https://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NODC/.WOA09/.Grid-1x1/.Annual/.temperature/.t_an/data.nc"
# netcdf_file = pygmt.which(fname=url, download=True)
# woa_temp = xr.open_dataset(netcdf_file).isel(time=0)

# fig = pygmt.Figure()
# fig.basemap(region="d", projection="N10c", frame=True)
# fig.grdimage(grid=woa_temp.t_an.sel(depth=0), cmap="SCM/batlow")
# fig.colorbar(frame=["xaf+lSea surface temperature", "y+l@.C"])

# fig.show()
# fig.savefig(fname="Fig5_PyGMT_xarray_sst.png")


# %%
import pygmt
import xarray as xr

grd_geoid = pygmt.datasets.load_earth_geoid()
# Create landmask: Set wet nodes to NaN and dry nodes to one
landmask = pygmt.grdlandmask(spacing="10m", region="d", maskvalues=["NaN", 1])
grd_mask = grd_geoid * landmask

fig = pygmt.Figure()
fig.basemap(region="d", projection="N10c", frame=True)
fig.grdimage(grid=grd_mask, cmap="SCM/vik")
fig.colorbar(frame=["xaf+lEarth geoid", "y+lm"], position="+nNaN")

fig.show()
fig.savefig(fname="Fig5_PyGMT_xarray_geoid.png")


# %%
import pygmt
from pygmt.datasets import load_mars_relief

mars = load_mars_relief(resolution="30m")
with pygmt.config(PROJ_ELLIPSOID="mars"):
    mars_filtered = mars.gmt.filter(filter="g500", distance=4)
    mars_gradient = mars_filtered.gmt.gradient(azimuth=-45, normalize="t1")

fig = pygmt.Figure()
pygmt.makecpt(cmap="batlow", series=[-6500, 6500])
fig.basemap(region="d", projection="H10c", frame=True)
fig.grdimage(mars, cmap=True, shading=True)
fig.shift_origin(yshift="-h-0.5c")
fig.basemap(region="d", projection="H10c", frame=True)
fig.grdimage(mars_filtered, cmap=True, shading=mars_gradient)
fig.colorbar(frame=["xa2000f1000+lElevation of Mars", "y+lm"], position="+e0.3c")

fig.show()
fig.savefig(fname="Fig5_PyGMT_xarray_mars.png")
