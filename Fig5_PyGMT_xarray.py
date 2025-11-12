import pygmt
import xarray as xr

url = "https://iridl.ldeo.columbia.edu/SOURCES/.NOAA/.NODC/.WOA09/.Grid-1x1/.Annual/.temperature/.t_an/data.nc"
netcdf_file = pygmt.which(fname=url, download=True)
woa_temp = xr.open_dataset(netcdf_file).isel(time=0)

fig = pygmt.Figure()
fig.grdimage(
    grid=woa_temp.t_an.sel(depth=0), cmap="SCM/batlow", projection="N10c", frame=True
)
fig.colorbar(frame=["xa5+lsea surface temperature", "y+l@.C"])
fig.show()

fig.savefig(fname="Fig5_PyGMT_xarray.png")
