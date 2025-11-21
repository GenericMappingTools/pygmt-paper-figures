import datetime

import pandas as pd
import pygmt

fig = pygmt.Figure()

fig.basemap(
    projection="X12c/6c",
    region=[datetime.date(2016, 1, 1), datetime.date(2026, 12, 31), -50, 1000],
    frame=["x+lYear", "y+lGitHub stars"],
)

for csvfile, color, label in zip(
    ["star_history_gmt.csv", "star_history_pygmt.csv", "star_history_gmtjl.csv"],
    ["238/86/52", "63/124/173", "170/121/193"],
    ["GMT", "PyGMT", "GMT.jl"],
):
    df = pd.read_csv(csvfile)
    df["Date"] = df["Date"].str.split(" \\(").str[0]
    df["Date"] = pd.to_datetime(df["Date"], format="%a %b %d %Y %H:%M:%S GMT%z", utc=True)

    fig.plot(x=df["Date"], y=df["Stars"], pen=color)
    fig.plot(x=df["Date"], y=df["Stars"], fill=color, style="a0.35c", label=label)

fig.legend(
    position="jTL+o0.1c+w1.9c",
    box=pygmt.params.Box(fill="gray95", pen="0.5p,gray50", radius="3p")
)

fig.show()
fig.savefig(fname="Fig7_PyGMT_datetime.png")
