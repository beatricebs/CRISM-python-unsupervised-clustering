import re
import numpy as np
from affine import Affine
import rasterio


def read_envi_georef(hdr_file):
    """
    Read an ENVI header (.hdr) file and extract:
    - upper-left corner coordinates
    - pixel size
    - CRS in WKT format

    Parameters
    ----------
    hdr_file : str
        Path to the ENVI .hdr file

    Returns
    -------
    x_ul : float
        X coordinate of the upper-left corner
    y_ul : float
        Y coordinate of the upper-left corner
    px : float
        Pixel size (assuming a square)
    crs_wkt : str
        CRS in WKT format
    """

    with open(hdr_file, "r") as f:
        text = f.read()

    # ---- map info ----
    map_info = re.search(
        r"map info\s*=\s*\{([^}]*)\}",
        text,
        re.IGNORECASE
    ).group(1)

    fields = [f.strip() for f in map_info.split(",")]

    #upper-left corner coordinates 
    x_ul = float(fields[3])
    y_ul = float(fields[4])

    #pixel size (meters)
    px = float(fields[5])

    #coordinate system (CRS)
    crs_wkt = re.search(
        r"coordinate system string\s*=\s*\{([^}]*)\}",
        text,
        re.IGNORECASE | re.DOTALL
    ).group(1).strip()

    return x_ul, y_ul, px, crs_wkt


def write_cluster_geotiff(
    out_path,
    rgb,
    x_ul,
    y_ul,
    px,
    crs_wkt
):
    """
    Write an RGB GeoTIFF from an array with shape (H, W, 3).

    Parameters
    ----------
    out_path : str
        Output GeoTIFF path
    rgb : np.ndarray
        RGB image array with shape (H, W, 3) and dtype uint8
    x_ul : float
        X coordinate of the upper-left corner
    y_ul : float
        Y coordinate of the upper-left corner
    px : float
        Pixel size
    crs_wkt : str
        CRS in WKT format
    """

    height, width, _ = rgb.shape

    #convert to rasterio format: (bands, rows, cols)
    rgb_rio = np.moveaxis(rgb, -1, 0)

    #affine transform (north-up image)
    transform = Affine(px, 0, x_ul, 0, -px, y_ul)

    with rasterio.open(
        out_path,
        "w",
        driver="GTiff",
        height=height,
        width=width,
        count=3,
        dtype="uint8",
        crs=crs_wkt,
        transform=transform,
        compress="lzw"
    ) as dst:
        dst.write(rgb_rio)