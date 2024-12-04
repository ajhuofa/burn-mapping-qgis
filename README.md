# BurnMapper QGIS Plugin

QGIS plugin for automated burn scar detection using Landsat NBR. Processes bands 4 (NIR) and 7 (SWIR).

## Features
- NBR calculation and thresholding
- Default threshold -0.2 (adjustable)
- Automatic polygon cleaning
- GDAL-based processing

## Requirements
- QGIS 3.0+
- GDAL
- NumPy

## Install
1. Copy to ~/.qgis3/python/plugins/
2. Enable in QGIS Plugin Manager

## Use
1. Load Landsat raster
2. Click BurnMapper icon
3. Adjust threshold
4. Run