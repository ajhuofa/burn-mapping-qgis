from qgis.core import *
from osgeo import gdal
import numpy as np

def process_burn_area(input_raster, roi, threshold=-0.2):
    ds = gdal.Open(input_raster)
    nir = ds.GetRasterBand(4).ReadAsArray()
    swir = ds.GetRasterBand(7).ReadAsArray()
    nbr = (nir - swir)/(nir + swir)
    return nbr * (nbr < threshold)

def clean_polygon_features(layer):
    # Remove small polygons and fix geometries
    for feat in layer.getFeatures():
        if feat.geometry().area() < min_area:
            layer.deleteFeature(feat.id())
    layer.commitChanges()