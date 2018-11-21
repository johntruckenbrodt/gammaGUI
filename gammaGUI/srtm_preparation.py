##############################################################
# preparation of srtm data for use in gamma
# module of software gammaGUI
# John Truckenbrodt 2014-15
# last update 2015-09-24
##############################################################

"""
The following tasks are performed by executing this script:
-reading of a parameter file dem.par
--see object par for necessary values; file is automatically created by starting the script via the GUI
-if necessary, creation of output and logfile directories
-generation of a DEM parameter file for each .hgt (SRTM) file in the working directory or its subdirectories
--the corresponding GAMMA command is create_dem_par, which is interactive. the list variables dempar and dempar2 are piped to the command line for automation
-if multiple files are found, mosaicing is performed
-replacement and interpolation of missing values
-transformation from equiangular (EQA) to UTM projection using a SLC parameter file
"""

import os
import re
import shutil
import zipfile
import subprocess as sp
from urllib2 import urlopen

import raster
from ancillary import finder, ReadPar, run, UTM, dissolve, HDRobject, hdr


def main():
    print "#############################################"
    print "preparing SRTM mosaic:"
    # read parameter textfile
    par = ReadPar(os.path.join(os.getcwd(), "PAR/srtm_preparation.par"))

    demdir = None
    if hasattr(par, "SRTM_archive"):
        if os.path.isdir(par.SRTM_archive):
            demdir = par.SRTM_archive

    parfiles = finder(os.getcwd(), ["*slc.par", "*mli.par", "*cal.par"])

    # define (and create) directories for processing results and logfile
    path_dem = os.path.join(os.getcwd(), "DEM/")
    path_log = os.path.join(os.getcwd(), "LOG/GEO/")
    for path in [path_log, path_dem]:
        if not os.path.exists(path):
            os.makedirs(path)

    # find SRTM tiles for mosaicing
    demlist = hgt_collect(parfiles, path_dem, demdir=demdir)

    # remove files created by this function
    for item in finder(path_dem, ["mosaic*", "dem*", "*.par"]):
        os.remove(item)

    if len(demlist) == 0:
        raise IOError("no hgt files found")

    # perform mosaicing if multiple files are found
    if len(demlist) > 1:
        print "mosaicing..."
        dem = os.path.join(path_dem, "mosaic")
        mosaic(demlist, dem)
    else:
        dem = demlist[0]
        dempar(dem)
    fill(dem, os.path.join(path_dem, "dem_final"), path_log)
    dem = os.path.join(path_dem, "dem_final")

    # transform DEM to UTM
    if par.utm == "True":
        print "transforming to UTM..."
        transform(dem, dem+"_utm", int(par.targetres))
        hdr(dem+"_utm.par")
    print "...done"
    print "#############################################"


def fill(dem, dem_out, logpath, replace=False):

    width = ReadPar(dem+".par").width

    path_dem = os.path.dirname(dem_out)

    rpl_flg = 0
    dtype = 4

    # replace values
    value = 0
    new_value = 1
    run(["replace_values", dem, value, new_value, dem+"_temp", width, rpl_flg, dtype], path_dem, logpath)

    value = -32768
    new_value = 0
    run(["replace_values", dem+"_temp", value, new_value, dem+"_temp2", width, rpl_flg, dtype], path_dem, logpath)

    # interpolate missing values
    r_max = 9
    np_min = 40
    np_max = 81
    w_mode = 2
    run(["interp_ad", dem+"_temp2", dem_out, width, r_max, np_min, np_max, w_mode, dtype], path_dem, logpath)

    # remove temporary files
    os.remove(dem+"_temp")
    os.remove(dem+"_temp2")

    # duplicate parameter file for newly created dem
    shutil.copy(dem+".par", dem_out+".par")

    # create ENVI header file
    hdr(dem_out+".par")

    if replace:
        for item in [dem+x for x in ["", ".par", ".hdr", ".aux.xml"] if os.path.isfile(dem+x)]:
            os.remove(item)


# transform SRTM DEM from EQA to UTM projection
def transform(infile, outfile, posting=90):

    # read DEM parameter file
    par = ReadPar(infile+".par")

    # transform corner coordinate to UTM
    utm = UTM(infile+".par")

    if os.path.isfile(outfile+".par"):
        os.remove(outfile+".par")
    if os.path.isfile(outfile):
        os.remove(outfile)

    # determine false northing from parameter file coordinates
    falsenorthing = "10000000." if "-" in par.corner_lat else "0"

    # create new DEM parameter file with UTM projection details
    inlist = ["UTM", "WGS84", 1, utm.zone, falsenorthing, outfile, "", "", "", "", "", "-"+str(posting)+" "+str(posting), ""]
    run(["create_dem_par", outfile+".par"], inlist=inlist)

    # transform dem
    run(["dem_trans", infile+".par", infile, outfile+".par", outfile, "-", "-", "-", 1])


# create GAMMA parameter text files for DEM files
# currently only EQA and UTM projections with WGS84 ellipsoid are supported
def dempar(dem, logpath=None):
    rast = raster.Raster(dem)

    # determine data type
    dtypes = {"Int16": "INTEGER*2", "UInt16": "INTEGER*2", "Float32": "REAL*4"}
    if rast.dtype not in dtypes:
        raise IOError("data type not supported")
    else:
        dtype = dtypes[rast.dtype]

    # format pixel posting and top left coordinate
    posting = str(rast.geotransform["yres"])+" "+str(rast.geotransform["xres"])
    latlon = str(rast.geotransform["ymax"])+" "+str(rast.geotransform["xmin"])

    # evaluate projection
    projections = {"longlat": "EQA", "utm": "UTM"}
    if rast.proj4args["proj"] not in projections:
        raise IOError("projection not supported (yet)")
    else:
        projection = projections[rast.proj4args["proj"]]

    # get ellipsoid
    ellipsoid = rast.proj4args["ellps"] if "ellps" in rast.proj4args else rast.proj4args["datum"]
    if ellipsoid != "WGS84":
        raise IOError("ellipsoid not supported (yet)")

    # create list for GAMMA command input
    parlist = [projection, ellipsoid, 1, os.path.basename(dem), dtype, 0, 1, rast.cols, rast.rows, posting, latlon]

    # execute GAMMA command
    run(["create_dem_par", os.path.splitext(dem)[0] + ".par"], os.path.dirname(dem), logpath, inlist=parlist)


# byte swapping from small to big endian (as required by GAMMA)
def swap(data, outname):
    rast = raster.Raster(data)
    dtype = rast.dtype
    if rast.format != "ENVI":
        raise IOError("only ENVI format supported")
    dtype_lookup = {"Int16": 2, "CInt16": 2, "Int32": 4, "Float32": 4, "CFloat32": 4, "Float64": 8}
    if dtype not in dtype_lookup:
        raise IOError("data type " + dtype + " not supported")
    sp.check_call(["swap_bytes", data, outname, str(dtype_lookup[dtype])], stdout=sp.PIPE)
    header = HDRobject(data+".hdr")
    header.byte_order = 1
    hdr(header, outname+".hdr")


# mosaicing of multiple DEMs
def mosaic(demlist, outname, byteorder=1, gammapar=True):
    nodata = str(raster.Raster(demlist[0]).nodata)
    run(dissolve(["gdalwarp", "-q", "-of", "ENVI", "-srcnodata", nodata, "-dstnodata", nodata, demlist, outname]))
    if byteorder == 1:
        swap(outname, outname+"_swap")
        for item in [outname, outname+".hdr", outname+".aux.xml"]:
            os.remove(item)
        os.rename(outname+"_swap", outname)
        os.rename(outname+"_swap.hdr", outname+".hdr")
    if gammapar:
        dempar(outname)


# concatenate hgt file names overlapping with multiple SAR scenes
# input is a list of GAMMA SAR scene parameter files
# this list is read for corner coordinates of which the next integer lower left latitude and longitude is computed
# hgt files are supplied in 1 degree equiangular format named e.g. N16W094.hgt (with pattern [NS][0-9]{2}[EW][0-9]{3}.hgt
# For north and east hemisphere the respective absolute latitude and longitude values are smaller than the lower left coordinate of the SAR image
# west and south coordinates are negative and hence the nearest lower left integer absolute value is going to be larger
def hgt(parfiles):
    lat = []
    lon = []
    for parfile in parfiles:
        out, err = sp.Popen(["SLC_corners", parfile], stdout=sp.PIPE).communicate()
        for line in out.split("\n"):
            # note: upper left and lower right, as computed by SLC_corners, define the bounding box coordinates and not those of the actual SAR image
            if line.startswith("upper left") or line.startswith("lower right"):
                items = filter(None, re.split("[\t\s]", line))
                # compute lower right coordinates of intersecting hgt tile
                lat.append(int(float(items[-2])//1))
                lon.append(int(float(items[-1])//1))

    # add missing lat/lon values and add an extra buffer of one degree
    lat = range(min(lat)-1, max(lat)+2)
    lon = range(min(lon)-1, max(lon)+2)

    # lat = range(min(lat), max(lat)+1)
    # lon = range(min(lon), max(lon)+1)

    # convert coordinates to string with leading zeros and hemisphere identification letter
    lat = [str(x).zfill(2+len(str(x))-len(str(x).strip("-"))) for x in lat]
    lat = [x.replace("-", "S") if "-" in x else "N"+x for x in lat]

    lon = [str(x).zfill(3+len(str(x))-len(str(x).strip("-"))) for x in lon]
    lon = [x.replace("-", "W") if "-" in x else "E"+x for x in lon]

    # concatenate all formatted latitudes and longitudes with each other as final product
    return [x+y+".hgt" for x in lat for y in lon]


# automatic downloading and unpacking of srtm tiles
# base directory must contain SLC files in GAMMA format including their parameter files for reading coordinates
# additional dem directory may locally contain srtm files. This directory is searched for locally existing files, which are then copied to the current working directory

def hgt_collect(parfiles, outdir, demdir=None):

    # concatenate required hgt tile names
    target_ids = hgt(parfiles)

    targets = []

    # define server and its subdirectories
    # tiff alternative (not implemented): ftp://srtm.csi.cgiar.org/SRTM_v41/SRTM_Data_GeoTIFF/
    server = "http://dds.cr.usgs.gov/srtm/version2_1/SRTM3/"
    continents = ["Africa", "Australia", "Eurasia", "Islands", "North_America", "South_America"]
    pattern = "[NS][0-9]{2}[EW][0-9]{3}"

    # if an additional dem directory has been defined, check this directory for required hgt tiles
    if demdir is not None:
        for item in finder(demdir, target_ids):
            targets.append(item)

    # check for additional potentially existing hgt tiles in the defined output directory
    for item in [os.path.join(outdir, x) for x in target_ids if os.path.isfile(os.path.join(outdir, x)) and not re.search(x, "\n".join(targets))]:
        targets.append(item)

    for item in targets:
        print item

    # search server for all required tiles, which were not found in the local directories
    if len(targets) < len(target_ids):
        print "searching for SRTM tiles on the server..."
        onlines = []
        for continent in continents:
            path = os.path.join(server, continent)
            response = urlopen(path).read()
            for item in re.findall(pattern+"[.]hgt.zip", response):
                outname = re.findall(pattern, item)[0]+".hgt"
                if outname in target_ids and outname not in [os.path.basename(x) for x in targets]:
                    onlines.append(os.path.join(path, item))
        onlines = list(set(onlines))

        for item in onlines:
            print item

        # if additional tiles have been found online, download and unzip them to the local directory
        if len(onlines) > 0:
            print "downloading {0} SRTM tiles...".format(len(onlines))
            for candidate in onlines:
                localname = os.path.join(outdir, re.findall(pattern, candidate)[0]+".hgt")
                infile = urlopen(candidate)
                with open(localname+".zip", "wb") as outfile:
                    outfile.write(infile.read())
                infile.close()
                with zipfile.ZipFile(localname+".zip", "r") as z:
                    z.extractall(outdir)
                os.remove(localname+".zip")
                targets.append(localname)
    return targets


if __name__ == '__main__':
    main()
