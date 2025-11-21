import pygmt

red, blue = "238/86/52", "#4B8BBE"  # GMT red and Python blue

fig = pygmt.Figure()
fig.basemap(region=[-1, 16, -0.5, 8], projection="x1c", frame=0)

# Add the GMT part.
fig.plot(x=[-0.5, 2.5, 2.5, -0.5], y=[0, 0, 6, 6], pen=f"2p,{red}", fill=f"{red}@70", close=True)
fig.vlines(x=1, ymin=1, ymax=3, pen="1.5p,gray30")
fig.vlines(x=1, ymin=3, ymax=5, pen="1.5p,gray30")
fig.plot(x=[1.0] * 3, y=[1, 3, 5], style="R2.1c/1c/3p", fill=red, pen="0.5p")
fig.text(
    x=[1.0] * 4,
    y=[1.25, 0.75, 3, 5],
    text=["GMT low-level", "library", "GMT C API", "GMT modules"] ,
    font="8p,1,white",
)
fig.logo(position="g1/6.95+jMC+w2.15c")

# Add the Python part.
fig.plot(x=[7.5, 15.5, 15.5, 7.5], y=[0, 0, 6, 6], pen=f"2p,{blue}", fill=f"{blue}@70", close=True)
for x, y in [
    ([10, 14], [1, 1]),
    ([10, 9], [1, 3]),
    ([9, 8.7], [3, 5]),
    ([9, 10.25], [3, 5]),
    ([10, 12], [1, 3]),
    ([12, 12], [3, 5]),
]:
    fig.plot(x=x, y=y, pen="1.5p,gray30")
fig.plot(x=[10, 9, 12], y=[1, 3, 3], style="R2.0c/1c/3p", fill=blue, pen="0.5p")
fig.plot(x=14, y=1, style="R2.0c/1c/3p", fill=blue, pen="0.5p")
fig.text(
    x=[10, 9, 12, 14],
    y=[1, 3, 3, 1],
    text=["NumPy", "Xarray", "pandas", "PyArrow"],
    font="8p,1,white",
)
fig.text(
    x=[8.7, 10.25, 12],
    y=[5, 5, 5],
    text=["rioxarray", "contextily", "GeoPandas"],
    font="8p,1,white",
    fill=blue,
    pen="0.5p,-",
    clearance="0.1c/0.1c+tO",
)
fig.image(
    "https://www.python.org/static/community_logos/python-logo-master-v3-TM.png",
    position="g11.5/7+jMC+w4.5c",  # 7.5 + (15.5 - 7.5)
    bitcolor="white+t",
)

# Add the PyGMT part.
fig.pygmtlogo(position="g5/2.65+jMC+w2c", wordmark="vertical")
fig.plot(
    data=[[2.6, 3, 3.9, 3], [6.1, 3, 7.4, 3]],
    style="v0.35c+a40+s+b+e+h0+ggray30",
    pen="2p,gray30",
)

fig.show()
fig.savefig("Fig2_PyGMT_ecosystem.png")