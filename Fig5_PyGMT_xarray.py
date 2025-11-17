import pygmt
import xarray as xr

url = "https://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NODC/.WOA09/.Grid-1x1/.Annual/.temperature/.t_an/data.nc"
netcdf_file = pygmt.which(fname=url, download=True)
woa_temp = xr.open_dataset(netcdf_file).isel(time=0)

fig = pygmt.Figure()
fig.basemap(region="d", projection="N10c", frame=True)
fig.grdimage(grid=woa_temp.t_an.sel(depth=0), cmap="SCM/batlow")
fig.colorbar(frame=["xaf+lSea surface temperature", "y+l@.C"])
fig.show()

# fig.savefig(fname="Fig5_PyGMT_xarray.png")


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

fig.savefig(fname="Fig5_PyGMT_xarray.png")
