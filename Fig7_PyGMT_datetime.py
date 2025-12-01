import requests
import pandas as pd

owner = "GenericMappingTools"
headers = {"Accept": "application/vnd.github.v3.star+json"}

for repo in ["gmt.jl", "pygmt", "gmt", "gmtmex"]:
    timestamps = []
    page = 1

    while True:
        r = requests.get(
            f"https://api.github.com/repos/{owner}/{repo}/stargazers",
            headers=headers,
            params={"per_page": 100, "page": page},
        )
        data = r.json()
        if not data:
            break

        timestamps += [s["starred_at"] for s in data]  # full ISO 8601 timestamp
        page += 1

    timestamps.sort()  # ISO strings sort chronologically

    df = pd.DataFrame({"timestamp": timestamps})
    df["cumulative_stars"] = range(1, len(df) + 1)

    print(df)
    df.to_csv(f"star_history_github_{repo}.csv", sep=";", index=False)



# %%
import datetime

import pandas as pd
import pygmt
from pygmt.params import Box

stars_step = 20

fig = pygmt.Figure()

fig.basemap(
    projection="X12c/6c",
    region=[datetime.date(2016, 1, 1), datetime.date(2026, 12, 31), -50, 1000],
    frame=["x+lYear", "ya100f50+lGitHub stars"],
)

for wrapper, file, color, symbol in zip(
    ["GMT", "GMT/MEX", "GMT.jl", "PyGMT"],
    ["gmt", "gmtmex", "gmt.jl", "pygmt"],
    ["238/86/52", "253/131/68", "149/88/178", "48/105/152"],
    ["C", "T", "I", "A"],
    strict=False,
):
    stars = pd.read_csv(f"star_history_github_{file}.csv", sep=";")
    fig.plot(data=stars, pen=color)
    fig.plot(data=stars[0:len(stars):stars_step], fill=color, style=f"{symbol}0.2c", label=wrapper)

fig.legend(
    position="jTL+o0.1c+w2.3", box=Box(fill="gray95", pen="0.5p,gray50", radius="3p"),
)

fig.show()
fig.savefig(fname="Fig7_PyGMT_datetime.png")
