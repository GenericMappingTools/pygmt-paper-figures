import pygmt

df_bath = pygmt.datasets.load_sample_data("bathymetry")
region_study = [
    min(df_bath.longitude),
    max(df_bath.longitude),
    min(df_bath.latitude),
    max(df_bath.latitude),
]

region_sel = [360 - 114, 360 - 111, 22, 26]
df_bath_sel = pygmt.select(data=df_bath, region=region_sel)

block_size = "10m"  # arc-minutes
# Count data points within each block
df_bath_sel_count = pygmt.blockmean(
    data=df_bath_sel, spacing=block_size, region=region_study, summary="n"
)
# Calculate mean bathymetry within each block
df_bath_sel_mean = pygmt.blockmean(
    data=df_bath_sel, spacing=block_size, region=region_study
)

# Convert tabular data to GMT-ready grid
grd_bath_sel_count = pygmt.xyz2grd(
    data=df_bath_sel_count, region=region_study, spacing=block_size
)
grd_bath_sel_mean = pygmt.xyz2grd(
    data=df_bath_sel_mean, region=region_study, spacing=block_size
)

# -----------------------------------------------------------------------------
fig = pygmt.Figure()

for block_value in ["counts", "mean bathymetry in meters"]:
    match block_value:
        case "counts":
            grd_block = grd_bath_sel_count
        case "mean bathymetry in meters":
            grd_block = grd_bath_sel_mean

    fig.coast(region=region_study, projection="M12c", land="gray", frame=True)

    # Plot all data points in black
    fig.plot(data=df_bath, style="p0.4p", fill="black")

    # Plot grid color-coded by number of data points within each block
    fig.grdimage(grid=grd_block, cmap="SCM/batlow", nan_transparent=True)
    fig.colorbar(frame=f"x+l{block_value} per block")

    # Plot data points within subregion in white
    fig.plot(data=df_bath_sel, style="p0.4p", fill="white")

    fig.shift_origin(xshift="w+2c")

fig.show()
