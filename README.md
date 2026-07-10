# PyGMT paper figures

[![GitHub License](https://img.shields.io/github/license/GenericMappingTools/pygmt-paper-figures?style=flat)](https://github.com/GenericMappingTools/pygmt-paper-figures/blob/main/LICENSE)
[![Digital Object Identifier for the Zenodo archive](https://img.shields.io/badge/DOI-10.5281/zenodo.19412361-blue)](https://doi.org/10.5281/zenodo.19412361)

This repository contains the Jupyter notebooks and supporting data used to generate the figures presented in the PyGMT paper:

> Tian, D., Fröhlich, Y., Leong, W. J., Grund, M., Schlitzer, W., Jones, M., Uieda, L., Luis, J. M. F. (2026).
> PyGMT: Bridging Python and the Generic Mapping Tools for Geospatial Visualization and Analysis.
> *Geochemistry, Geophysics, Geosystems*, 27, e2026GC013105. https://doi.org/10.1029/2026GC013105

[![](https://github.com/GenericMappingTools/pygmt-paper-figures/pygmt_paper_figures_overview_github.png)](https://doi.org/10.1029/2026GC013105)

## Files

- [`Fig1_PyGMT_GMT_comparison.ipynb`](Fig1_PyGMT_GMT_comparison.ipynb): Example comparison of GMT CLI (Bash) and PyGMT (Python) scripts
- [`Fig2_PyGMT_ecosystem.ipynb`](Fig2_PyGMT_ecosystem.ipynb): The PyGMT ecosystem
- [`Fig3_PyGMT_backgrounds.ipynb`](Fig3_PyGMT_backgrounds.ipynb): Different types of geographic background basemaps of Iceland
- [`Fig4_PyGMT_pandas.ipynb`](Fig4_PyGMT_pandas.ipynb): Seismicity along the Andaman-Sumatra-Java Subduction Zone
- [`Fig5_PyGMT_xarray.ipynb`](Fig5_PyGMT_xarray.ipynb): Hemispherical views of long-wavelength Mars topography
- [`Fig6_PyGMT_geopandas.ipynb`](Fig6_PyGMT_geopandas.ipynb): Choropleth map of the population in the US
- [`Fig7_PyGMT_datetime.ipynb`](Fig7_PyGMT_datetime.ipynb): GitHub star history of GMT and the wrappers
- `star_history_github_*.csv`: Cached GitHub stars data used by Figure 7

|Figure 1 | Figure 2 | Figure 3 |
| --- | --- | --- |
| ![](https://agupubs.onlinelibrary.wiley.com/cms/asset/2b2ee924-bee1-4372-969c-60915d63a342/ggge22002-fig-0001-m.jpg) | ![](https://agupubs.onlinelibrary.wiley.com/cms/asset/c4dd8aba-a0f1-477e-b977-988542856159/ggge22002-fig-0002-m.jpg) | ![](https://agupubs.onlinelibrary.wiley.com/cms/asset/818d8d41-b83c-477c-8994-b3672dd95b41/ggge22002-fig-0003-m.jpg) |

## Environment setup

These notebooks require GMT, PyGMT, and other dependencies to be installed in the same environment.
The `environment.yml` file can be used to create a conda environment with all the required dependencies.

Create and activate the environment:
```bash
conda env create -f environment.yml
conda activate pygmt-paper-figures
```

## Running the notebooks

Start JupyterLab inside the activated environment:

```bash
jupyter lab
```

Then open the notebooks and run them within the `pygmt-paper-figures` environment.

## Notes

- Some figures download remote resources or rely on online datasets.
- Figure outputs are typically saved as PNG files from within the notebooks.

## Citation

Notebooks in this repository are archived on Zenodo and can be cited as:

> Tian, D., Fröhlich, Y., Grund, M., Schlitzer, W., & Leong, W. J. (2026).
> Reproducible materials for "PyGMT: Bridging Python and the Generic Mapping Tools for Geospatial Visualization and Analysis".
> Zenodo. https://doi.org/10.5281/zenodo.19412361

## License

This repository is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
