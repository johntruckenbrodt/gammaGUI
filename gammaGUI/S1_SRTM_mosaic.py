##############################################################
# SRTM 3 arcsec .hgt mosaicing for Sentinel-1 processing
# John Truckenbrodt 2015-08-12
##############################################################

"""
The following tasks are performed by executing this script:
-read a S1 meta data csv file and extract corner coordinates for the scene to be processed
-search a defined srtm directory for all tiles which overlap with the S1 scene based on the extracted coordinates
-if more than one hgt tile is required, mosaic all; if not rename the file
-if the transform option is selected, the resulting DEM will be transformed to UTM projection
"""
import sys

import os
import re
import csv
import shutil
import argparse

import S1_meta_extract
from ancillary import finder
from srtm_preparation import dempar, mosaic, hgt, transform

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--transform', action='store_true', help='transform the final DEM to UTM coordinates')
parser.add_argument('zipfile', nargs=1, help='S1 zipped scene archive to be used')
parser.add_argument('outdir', nargs=1, help='output directory')
parser.add_argument('srtmdir', nargs=1, help='directory containing SRTM hgt tiles')
args = parser.parse_args()

zipfile = args.zipfile[0]
outdir = args.outdir[0]
srtmdir = args.srtmdir[0]

# the working directory is assigned to be the directory containing the zipped S1 scene
dir_scene = os.path.dirname(zipfile)

# concatenate output SRTM mosaic name and abort script if file already exists
name_dem = os.path.join(outdir, os.path.basename(zipfile)[:-4] + "_srtm")
if os.path.isfile(name_dem):
    sys.exit("SRTM mosaic already exists")

# scan S1 meta data file csv file (assumed to be named meta.csv in the same directory as the zipped S1 file
csvname = os.path.join(dir_scene, "meta.csv")

if not os.path.isfile(csvname):
    S1_meta_extract.main(dir_scene, os.path.join(dir_scene, "meta.csv"))

lat = lon = []
with open(csvname, "r") as csvfile:
    for row in csv.DictReader(csvfile):
        if re.search(os.path.basename(zipfile), row["zipFilename"]):
            lat = [row["upperLeftLat"], row["lowerRightLat"]]
            lon = [row["upperLeftLon"], row["lowerRightLon"]]
            break

# concatenate names of required srtm tiles with convention "[NS][0-9]{2}[EW][0-9]{3}.hgt"
if len(lat) > 0 and len(lon) > 0:
    target_ids = hgt(lat, lon)
else:
    raise IOError("meta data entry missing")

# search for required tiles in the defined srtm directory
targets = finder(srtmdir, target_ids)

# check whether all required tiles were found and copy them to the working directory
if len(targets) < len(target_ids):
    raise IOError("missing hgt files")
else:
    for item in targets:
        shutil.copy(item, outdir)
targets = [os.path.join(outdir, x) for x in target_ids]

# create gamma parameter files for all DEMs
dempar(targets)

# perform mosaicing if necessary
if len(targets) > 1:
    mosaic(targets, name_dem)
    # remove hgt files from temporary directory
    for item in targets:
        os.remove(item)
        os.remove(item + ".par")
else:
    os.rename(targets[0], name_dem)
    os.rename(targets[0] + ".par", name_dem + ".par")

if args.transform:
    transform(infile=name_dem, outfile=name_dem + "_utm", posting=90)
    os.remove(name_dem)
    os.remove(name_dem+".par")
    os.rename(name_dem + "_utm", name_dem)
    os.rename(name_dem + "_utm.par", name_dem+".par")
    if os.path.isfile(name_dem + "_utm.hdr"):
        os.rename(name_dem + "_utm.hdr", name_dem + ".hdr")
