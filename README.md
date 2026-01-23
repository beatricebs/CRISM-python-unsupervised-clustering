# CRISM-python-unsupervised-clustering

## Introduction
This repository contains the code to perform unsupervised clustering on CRISM hyperspectral data. 

## Dataset

- Type of data: [CRISM Map-Projected Targeted Reduced Data Record (MTRDR)](https://ode.rsl.wustl.edu/mars/pagehelp/Content/Missions_Instruments/Mars%20Reconnaissance%20Orbiter/CRISM/CRISM%20Product%20Primer/CRISM%20MTRDR.htm).
- Access to dataset: [NASA - PDS Geoscience Node](https://pds-geosciences.wustl.edu/missions/messenger/index.htm).

## Requirements

**Tested with Python 3.9.12**
- Important: UMAP won't work with Python versions >= 3.10

**Library versions**

| Library | Version |
|--------|---------|
| numpy | 1.21.6 |
| pandas | 2.0.3 |
| matplotlib | 3.5.1 |
| colorcet | 1.0.0 |
| spectral | 0.23.1 |
| scikit-image | 0.19.2 |
| scikit-learn | 1.6.1 |
| rasterio | 1.3.6 |
| affine | 2.4.0 |
| umap | 0.5.3 |

## Acknowledgements
This code has been developed in collaboration with Dr. Mario D'Amore (DLR, Berlin, Germany).

## License
MIT
