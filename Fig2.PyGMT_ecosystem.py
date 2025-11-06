#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pygmt

fig = pygmt.Figure()
fig.basemap(region=[-1, 16, -1, 7], projection="x1c", frame="+n")

red, blue = "238/86/52", "#4B8BBE"

x1 = 1.0
fig.plot(x=[x1 - 1.5, x1 + 1.5, x1 + 1.5, x1 - 1.5], y=[0, 0, 6, 6], pen="1p,black", close=True)
fig.vlines(x=x1, ymin=1, ymax=3, pen="1p,black")
fig.vlines(x=x1, ymin=3, ymax=5, pen="1p,black")
fig.plot(x=[x1] * 3, y=[1, 3, 5], style="R2.1c/1c/3p", fill=red, pen="0.5p,black")
fig.text(
    x=[x1] * 4, 
    y=[1.25, 0.75, 3, 5], 
    text=["GMT low-level", "library", "GMT C API", "GMT modules"] , 
    font="8p,1,white",
)
fig.logo(position=f"g{x1}/7+jMC+w3c")


fig.plot(x=[10, 14], y=[1, 1], pen="1p,black")
fig.plot(x=[10, 9], y=[1, 3], pen="1p,black")
fig.plot(x=[9, 8.7], y=[3, 5], pen="1p,black")
fig.plot(x=[9, 10.25], y=[3, 5], pen="1p,black")
fig.plot(x=[10, 12], y=[1, 3], pen="1p,black")
fig.plot(x=[12, 12], y=[3, 5], pen="1p,black")

fig.plot(x=[7.5, 15.5, 15.5, 7.5], y=[0, 0, 6, 6], pen="1p,black", close=True)
fig.plot(x=[10, 9, 12], y=[1, 3, 3], style="R2.0c/1c/3p", fill=blue, pen="0.5p,black")
fig.plot(x=14, y=1, style="R2.0c/1c/3p", fill=blue, pen="0.5p,black,-")
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
    pen="0.5p,black,-",
    clearance="0.1c/0.1c+tO",
)
fig.logo(position="g12/7+jMC+w3c")

fig.pygmtlogo(position="g5/2.75+jMC+w2c", wordmark="vertical")
fig.plot(
    data=[[2.5, 3, 3.75, 3], [6.25, 3, 7.5, 3]], 
    style="v0.4c+s+b+e+gblack", 
    pen="2p"
)

fig.show()


# In[ ]:




