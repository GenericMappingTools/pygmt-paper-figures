import requests
import pandas as pd

def get_star_history(repo):
    owner = "GenericMappingTools"
    headers = {
        "Accept": "application/vnd.github.v3.star+json",
        # "Authorization": "Bearer {YOUR_GITHUB_TOKEN_HERE}",
    }

    timestamps, users = [], []
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
        users += [s["user"]["login"] for s in data]
        page += 1
    df = pd.DataFrame({"timestamp": timestamps, "user": users}).sort_values("timestamp")
    df.to_csv(f"star_history_github_{repo}.csv", sep=",", index=False)


for repo in ["gmt", "pygmt", "gmt.jl", "gmtmex"]:
    get_star_history(repo)

# %%
import datetime

import pandas as pd
import pygmt
from pygmt.params import Box

fig = pygmt.Figure()
fig.basemap(
    projection="X12c/6c",
    region=[datetime.date(2016, 1, 1), datetime.datetime.now(), -50, 1000],

    frame=["x+lYear", "ya100f50+lGitHub stars"],
)

for wrapper, file, color, symbol in zip(
    ["GMT", "PyGMT", "GMT.jl", "GMT/MEX"],
    ["gmt", "pygmt", "gmt.jl", "gmtmex"],
    ["238/86/52", "48/105/152", "149/88/178", "230/51/51"],
    ["C", "A", "T", "I"],
    strict=False,
):
    df = pd.read_csv(
        f"star_history_github_{file}.csv",
        parse_dates=["timestamp"],
        index_col="timestamp",
    )
    df = df.resample("6ME").count().cumsum().rename(columns={"user": "stars"})
    fig.plot(x=df.index, y=df["stars"], pen=color)
    fig.plot(
        x=df.index, y=df["stars"], style=f"{symbol}0.2c", fill=color, label=wrapper
    )
fig.legend(
    position="jTL+o0.1c+w2.3", box=Box(fill="gray95", pen="0.5p,gray50", radius="3p"),
)

fig.show()
fig.savefig(fname="Fig7_PyGMT_datetime.png")
