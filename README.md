# CRISM-python-unsupervised-clustering

## Introduction
This repository contains the code to perform unsupervised clustering on CRISM hyperspectral data. 

## Dataset

- Type of data: [CRISM Map-Projected Targeted Reduced Data Record (MTRDR)](https://ode.rsl.wustl.edu/mars/pagehelp/Content/Missions_Instruments/Mars%20Reconnaissance%20Orbiter/CRISM/CRISM%20Product%20Primer/CRISM%20MTRDR.htm). 
- Access to dataset: [NASA - PDS Geoscience Node](https://pds-geosciences.wustl.edu/missions/messenger/index.htm).

Please download: 
1) IF cube, composed of three files with the following extensions: .img, .hdr, .lbl (example of filename: frt0000bef5_07_if165j_mtr3); 
2) SR cube, the refined summary parameter cube, composed of three files with the following extensions: .img, .hdr, .lbl (example of filename: frt0000bef5_07_sr165j_mtr3); 
3) wavelenghth file, composed of two files with the extensions .tab and .lbl (example of filename: (frt00009b5a_07_wv165j_mtr3).

## Requirements

**Tested on x86-64 architecture with Python 3.9.12**
- Important: UMAP won't work with Python versions >= 3.10
- A virtual environment to avoid dependency conflicts is highly suggested
- We also recommend installing umap-learn and rasterio first, then installing the other dependencies.

**Library versions**

| Library | Version |
|--------|---------|
| numpy | 2.0.2 |
| pandas | 2.3.3 |
| matplotlib | 3.9.4 |
| colorcet | 3.1.0 |
| spectral | 0.24.0 |
| scikit-image | 0.24.0 |
| scikit-learn | 1.6.1 |
| rasterio | 1.4.3 |
| affine | 2.4.0 |
| umap-learn | 0.5.12 |

## Acknowledgements
This code has been developed in collaboration with Dr. Mario D'Amore (DLR, Berlin, Germany).

## License
MIT
