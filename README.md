# PyGMT paper figures

This repository contains the Jupyter notebooks and supporting data used to generate the figures presented in the PyGMT paper.

## Files

- [`Fig1_PyGMT_GMT_comparison.ipynb`](Fig1_PyGMT_GMT_comparison.ipynb)
- [`Fig2_PyGMT_ecosystem.ipynb`](Fig2_PyGMT_ecosystem.ipynb)
- [`Fig3_PyGMT_backgrounds.ipynb`](Fig3_PyGMT_backgrounds.ipynb)
- [`Fig4_PyGMT_pandas.ipynb`](Fig4_PyGMT_pandas.ipynb)
- [`Fig5_PyGMT_xarray.ipynb`](Fig5_PyGMT_xarray.ipynb)
- [`Fig6_PyGMT_geopandas.ipynb`](Fig6_PyGMT_geopandas.ipynb)
- [`Fig7_PyGMT_datetime.ipynb`](Fig7_PyGMT_datetime.ipynb)
- `star_history_github_*.csv`: cached data used by Figure 7

## Environment setup

These notebooks require a **development version of PyGMT**. The environment definition
in `environment.yml` currently installs PyGMT from TestPyPI:

- GMT: `6.6.0`
- pygmt: `0.19.0.dev100`

Create and activate the environment:

```bash
conda env create -f environment.yml
conda activate pygmt-paper-figures
```

## Figure-specific note

`Fig1_PyGMT_GMT_comparison.ipynb` and `Fig2_PyGMT_ecosystem.ipynb` depend on PyGMT
features that are available on specific development branches which are not merged into
the main branch of PyGMT yet.

Install the matching branch before running each notebook:

- `Fig1_PyGMT_GMT_comparison.ipynb`: requires the `feature/paragraph` branch

```bash
pip install --force-reinstall "git+https://github.com/GenericMappingTools/pygmt.git@feature/paragraph"
```

- `Fig2_PyGMT_ecosystem.ipynb`: requires the `code-pygmt-logo` branch

```bash
pip install --force-reinstall "git+https://github.com/GenericMappingTools/pygmt.git@code-pygmt-logo"
```

## Running the notebooks

Start JupyterLab inside the activated environment:

```bash
jupyter lab
```

Then open the notebooks and run them within the `pygmt-paper-figures` environment.

## Notes

- The notebooks expect GMT to be available through the same environment.
- Some figures download remote resources or rely on online datasets.
- Figure outputs are typically saved as PNG files from within the notebooks.
