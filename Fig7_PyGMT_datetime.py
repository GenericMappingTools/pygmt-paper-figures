import datetime

import pandas as pd
import pygmt
from pygmt.params import Box


fig = pygmt.Figure()

fig.basemap(
    projection="X12c/6c",
    region=[datetime.date(2016, 1, 1), datetime.date(2026, 12, 31), -50, 1000],
    frame=["x+lYear", "ya100f50+lGitHub stars"],
)

for wrapper, file, color, symbol in zip(
    ["GMT", "GMT/MEX", "GMT.jl", "PyGMT"],
    ["gmt", "gmtmex", "gmtjl", "pygmt"],
    ["238/86/52", "253/131/68", "149/88/178", "48/105/152"],
    ["C", "T", "I", "A"],
    strict=False,
):
    df = pd.read_csv(f"star_history_{file}.csv")
    df["Date"] = df["Date"].str.split(" \\(").str[0]
    df["Date"] = pd.to_datetime(
        df["Date"], format="%a %b %d %Y %H:%M:%S GMT%z", utc=True
    )

    fig.plot(x=df["Date"], y=df["Stars"], pen=color)
    fig.plot(x=df["Date"], y=df["Stars"], fill=color, style=f"{symbol}0.2c", label=wrapper)

fig.legend(
    position="jTL+o0.1c+w2.3", box=Box(fill="gray95", pen="0.5p,gray50", radius="3p"),
)

fig.show()
fig.savefig(fname="Fig7_PyGMT_datetime.png")
