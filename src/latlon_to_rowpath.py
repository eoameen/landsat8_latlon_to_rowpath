
import argparse
import numpy as np
from osgeo import ogr
import shapely.wkt
import shapely.geometry


def _validate_input(lat: float, lon: float, mode: str) -> bool:
    """validate input provided by the user"""
    # validate mode
    if mode not in ["A", "D"]:
        raise ValueError("Incorrect mode. Choose either A or D")

    # validate lat-lon pair (signed degrees fomat (DDD.dddd))
    if not ((lat >= -90.0) and (lat <= 90.0)):
        raise ValueError(
            "Incorrect latitude value. Enter a value between -90.0 and 90.0"
        )
    elif not ((lon >= -180.0) and (lon <= 180.0)):
        raise ValueError(
            "Incorrect longitude value. Enter a value between -180.0 and 180.0"
        )

    return True


def latlon_to_rowpath(lat: float, lon: float, mode: str) -> list:
    """convert lat/lon coordinates to landsat-8 row/path pair(s)"""

    # validate input
    _validate_input(lat, lon, mode)

    # load shapefile
    if mode == "D":
        shapefile = "shapefiles/WRS2_descending_0/WRS2_descending.shp"
    else:
        shapefile = "shapefiles/WRS2_ascending_0/WRS2_acsending.shp"
    wrs = ogr.Open(shapefile)
    layer = wrs.GetLayer(0)

    # make a point
    point = shapely.geometry.Point(lon, lat)

    # find all features that contain the input point
    pairs = []
    for i in np.arange(layer.GetFeatureCount()):
        feature = layer.GetFeature(i)
        geom = feature.GetGeometryRef()
        shape = shapely.wkt.loads(geom.ExportToWkt())
        if point.within(shape) and feature["MODE"] == mode:
            pairs.append([feature["ROW"], feature["PATH"]])

    return pairs


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--latitude",
        help="Latitude in signed degrees fomat (DDD.dddd)",
        type=float,
        required=True,
    )
    parser.add_argument(
        "-n",
        "--longitude",
        help="Longitude in signed degrees fomat (DDD.dddd)",
        type=float,
        required=True,
    )
    parser.add_argument(
        "-m",
        "--mode",
        help="Choose either daytime captures (D) or nighttime captures (A)",
        type=str,
        required=True,
    )
    args = parser.parse_args()
    latlon_to_rowpath(args.latitude, args.longitude, args.mode)
