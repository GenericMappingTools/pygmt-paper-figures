# %%
import pygmt

red, blue = "238/86/52", "#4B8BBE"  # GMT red and Python blue

fig = pygmt.Figure()
fig.basemap(region=[-1, 16, -1, 8], projection="x1c", frame="+n")

# Add the GMT part.
fig.plot(x=[-0.5, 2.5, 2.5, -0.5], y=[0, 0, 6, 6], pen="1p", close=True)
fig.vlines(x=1, ymin=1, ymax=3, pen="1p")
fig.vlines(x=1, ymin=3, ymax=5, pen="1p")
fig.plot(x=[1.0] * 3, y=[1, 3, 5], style="R2.1c/1c/3p", fill=red, pen="0.5p")
fig.text(
    x=[1.0] * 4,
    y=[1.25, 0.75, 3, 5],
    text=["GMT low-level", "library", "GMT C API", "GMT modules"] ,
    font="8p,1,white",
)
fig.logo(position="g1/7+jMC+w2c")

# Add the Python part.
fig.plot(x=[7.5, 15.5, 15.5, 7.5], y=[0, 0, 6, 6], pen="1p", close=True)
for x, y in [
    ([10, 14], [1, 1]),
    ([10, 9], [1, 3]),
    ([9, 8.7], [3, 5]),
    ([9, 10.25], [3, 5]),
    ([10, 12], [1, 3]),
    ([12, 12], [3, 5]),
]:
    fig.plot(x=x, y=y, pen="1p")
fig.plot(x=[10, 9, 12], y=[1, 3, 3], style="R2c/1c/3p", fill=blue, pen="0.5p")
fig.plot(x=14, y=1, style="R2c/1c/3p", fill=blue, pen="0.5p,dashed")
fig.text(
    x=[10, 9, 12, 14],
    y=[1, 3, 3, 1],
    text=["NumPy", "Xarray", "Pandas", "PyArrow"],
    font="8p,1,white",
)
fig.text(
    x=[8.7, 10.25, 12],
    y=[5, 5, 5],
    text=["rioxarray", "contextily", "GeoPandas"],
    font="8p,1,white",
    fill=blue,
    pen="0.5p,dashed",
    clearance="0.1c/0.1c+tO",
)
fig.image(
    "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
    position="g12/7+jMC+w4.5c"
)

# Add the PyGMT part.
fig.pygmtlogo(position="g5/2.65+jMC+w2c", wordmark="vertical")
fig.plot(
    data=[[2.6, 3, 3.9, 3], [6.1, 3, 7.4, 3]],
    style="v0.4c+s+b+e+gblack",
    pen="2p",
)

fig.show()
fig.savefig("Fig2.PyGMT_ecosystem.png")

# %%



