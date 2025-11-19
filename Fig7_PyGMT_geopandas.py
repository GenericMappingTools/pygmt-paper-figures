import geopandas as gpd
import pygmt

fig = pygmt.Figure()

fig.basemap(region=[-88, -87.5, 41.64, 42.04], projection="M9c", frame="rtlb")

gdf_airbnb = gpd.read_file("https://geodacenter.github.io/data-and-lab//data/airbnb.zip")
popul_min = gdf_airbnb["population"].min()
popul_max = gdf_airbnb["population"].max()

pygmt.makecpt(cmap="SCM/bilbao", series=[popul_min, popul_max, 10])
fig.colorbar(frame="x+lpopulation", position="jBL+jBL+o0.5c/0c+v")
fig.plot(
    data=gdf_airbnb,
    pen="0.2p,gray10",
    fill="+z",
    cmap=True,
    aspatial="Z=population",
)

fig.show()
fig.savefig(fname="Fig7_PyGMT_geopandas.png")


# %%
import pygmt
import geopandas as gpd

world = gpd.read_file("https://naciscdn.org/naturalearth/50m/cultural/ne_50m_admin_0_countries.zip")
rivers = gpd.read_file("https://naciscdn.org/naturalearth/110m/physical/ne_110m_rivers_lake_centerlines.zip")
cities = gpd.read_file("https://naciscdn.org/naturalearth/110m/cultural/ne_110m_populated_places_simple.zip")

world["POP_EST"] *= 1.0e-5

fig = pygmt.Figure()
fig.basemap(region="=SA", projection="M15c", frame=True)
fig.plot(data=world, pen="0.5p,black", fill="lightgreen")
pygmt.makecpt(cmap="turbo", series=(0, 3000, 100))
fig.plot(
    data=world,
    pen="0.2p,gray10",
    fill="+z",
    cmap=True,
    aspatial="Z=POP_EST",
)
fig.colorbar(frame=True)
fig.plot(data=rivers, pen="1p,blue")
fig.plot(data=cities, style="c0.1c", fill="red", pen="black")
fig.text(
    x=cities.geometry.x,
    y=cities.geometry.y,
    text=cities["name"],
    font="10p,Helvetica-Bold,black",
    offset="0.2c/0.2c",
)
fig.show()


# %%
import pandas as pd
import pygmt


# %%
# -----------------------------------------------------------------------------
# General stuff
# -----------------------------------------------------------------------------
color_neg = "darkorange"
color_pos = "darkgreen"
color_null = "white"

lon_min = -26
lon_max = 52
lat_min = 33
lat_max = 72

region = [lon_min, lon_max, lat_min, lat_max]
projection="M10c"


# %%
# -----------------------------------------------------------------------------
# Load data
# -----------------------------------------------------------------------------
data_file = "eu_population.txt"
df_pop_raw = pd.read_csv(f"{data_file}", sep="\t")

sort_by = "change_percent"  # "land", "change_percent"
df_pop = df_pop_raw.sort_values(sort_by, ignore_index=True)

abs_max_change = abs(max(df_pop["change_percent"]))


# %%
# -----------------------------------------------------------------------------
# Create map
# -----------------------------------------------------------------------------
fig = pygmt.Figure()
fig.basemap(region=region, projection=projection, frame=True)

for i_land in range(len(df_pop)):

    land = df_pop["land"][i_land]
    change = df_pop["change_percent"][i_land]

    # Creat simple diverging colormap via semi-transparency
    color_sign = color_pos
    if change < 0: color_sign = color_neg
    elif change == 0: color_sing = color_null
    color_trans = f"{color_sign}@{abs_max_change - abs(change)}"

    # Make a choropleth map using dcw
    fig.coast(dcw=f"{land}+g{color_trans}")

    # Plot dummy data points outside of study area for legend
    leg_head = " "
    if i_land == 0:
        leg_head = "+N2+HPopulation change 1990 - 2023+f11p"
    fig.plot(
        x=0,
        y=0,
        style="s0.4c",
        fill=color_trans,
        pen="0.1p,gray30",
        label=f"{land}: {change} %{leg_head}",
    )

    print(land)
    # fig.show()

# Add shorelines and political boundaries
fig.coast(shorelines="1/0.1p,gray60", borders="1/0.3p,white")

# Add legend
with pygmt.config(FONT="9p"):
    fig.legend(position="JRM+jLM+o0.2c/0c+w7.5c")

# Show and save figure
fig.show()
fig_name = f"dcw_choropleth_sorted_by_{sort_by}"
for ext in ["png"]: #, "pdf", "eps"]:
    fig.savefig(fname=f"{fig_name}.{ext}")
