#!/usr/bin/env python2.7
##############################################################
# geocoding of Sentinel-1 GRD data
# John Truckenbrodt 2015
# last update 2015-09-24
##############################################################

"""
The following tasks are performed by executing this script:
-unzipping of a S1 scene directory
-conversion into GAMMA format
-multilooking to retrieve approximately square pixels (20 m resolution)
-mosaicing of all SRTM HGT tiles overlapping with the SAR image
-interpolation of SRTM data gaps
-forward geocoding and pixel area computation for one polarization
-backward geocoding, topographic normalization, conversion to dB and export to GeoTiff for all polarizations
the script supports the following additional options, which are to be added to its console call:
-l create logfiles?
-i keep intermediate files (which are stored in the temporary directory)?
-t transform the supplied DEM to UTM?
further information is given upon calling "python S1_main.py -h"
the output product will contain of a GeoTiff and the original annotation xml file for each polarization, a quicklook kml and png and,
in case the logfile option was set, a folder containing logfiles for each of the processing steps
"""

import sys
import math
import os
import re
import shutil
import zipfile as zf

from ancillary import run, finder, ReadPar

try:
    import argparse
except ImportError:
    try:
        os.remove(os.path.join(os.path.dirname(sys.argv[0]), "locale.pyc"))
    finally:
        import argparse

from time import asctime

import srtm_preparation as srtm


def main(zipfile, tempdir, outdir, srtmdir, transform, logfiles, intermediates):


    # Definition geocode_back interpolation function
    # method 1: negative values possible (e.g. in urban areas) - use method 2 to avoid this
    # 0 - Nearest Neighbor
    # 1 - Bicubic Spline
    # 2 - Bicubic Spline-Log
    func_geoback = 2

    # function for interpolation of layover/shadow/foreshortening/DEM gaps
    # 0: set to 0; 1: linear interpolation; 2: actual value; 3: nn-thinned
    func_interp = 0

    # define target resolution; multilooking factors will be computed automatically
    res_target = 20

    # set DEM resolution and compute oversampling factor
    res_dem = 100
    dem_ovs = res_dem//res_target

    print "##########################################\n%s\n-------------\nprocessing started: %s\n" % (zipfile[:-4], asctime())

    ######################################################################

    pattern = r"^(?P<sat>S1[AB])_(?P<beam>S1|S2|S3|S4|S5|S6|IW|EW|WV|EN|N1|N2|N3|N4|N5|N6|IM)_(?P<prod>SLC|GRD|OCN)(?:F|H|M|_)_(?:1|2)(?P<class>S|A)(?P<pols>SH|SV|DH|DV|HH|HV|VV|VH)_(?P<start>[0-9]{8}T[0-9]{6})_(?P<stop>[0-9]{8}T[0-9]{6})_(?:[0-9]{6})_(?:[0-9A-F]{6})_(?:[0-9A-F]{4})\.SAFE$"

    # unzip the dataset
    try:
        with zf.ZipFile(zipfile, "r") as z:
            scene = sorted(z.namelist())[0].strip("/")
            match = re.match(pattern, scene)
            orbit = "D" if float(re.findall("[0-9]{6}", match.group("start"))[1]) < 120000 else "A"
            outname_base = "_".join([os.path.join(outdir, match.group("sat")), match.group("beam"), match.group("start").replace("T", "_"), orbit])

            if not os.path.exists(os.path.join(tempdir, scene)) and len(finder(outdir, [os.path.basename(outname_base)], regex=True)) == 0:
                if not z.testzip():
                    print "unzipping data..."
                    # print z.testzip()
                    z.extractall(tempdir)
                else:
                    print "corrupt zip"
                    return
            else:
                print "file already imported/processed"
                return
            tempdir = os.path.join(tempdir, scene)
    except ImportError:
        print "...skipped"
        return

    # create logfile folder if this option was selected
    if logfiles:
        path_log = outname_base+"_log"
        if os.path.exists(path_log):
            shutil.rmtree(path_log)
        os.makedirs(path_log)
    else:
        path_log = None

    ######################################################################
    print "converting to GAMMA format..."
    try:
        run([sys.executable, os.path.join(os.getcwd(), "reader.py"), tempdir], outdir=tempdir, logpath=path_log)
    except ImportError:
        print "...failed"
        return

    # gather all imported files
    files_mli = finder(tempdir, ["*_mli"])

    # compute multilooking factors
    par = ReadPar(files_mli[0]+".par")
    rlks = int(round(res_target/float(par.range_pixel_spacing)))
    azlks = int(round(res_target/float(par.azimuth_pixel_spacing)))

    # perform multilooking
    for item in files_mli:
        run(["multi_look_MLI", item, item+".par", item[:-3]+"mli2", item[:-3]+"mli2.par", rlks, azlks], logpath=path_log)

    # gather all newly created MLIs
    files_mli = finder(tempdir, ["*_mli2"])

    # select master image
    master = files_mli[0]

    base = "_".join(master.split("_")[:-1])+"_"
    dem_seg = base+"dem"
    lut = base+"lut"
    lut_fine = base+"lut_fine"
    sim_sar = base+"sim_sar"
    u = base+"u"
    v = base+"v"
    inc = base+"inc"
    psi = base+"psi"
    pix = base+"pix"
    ls_map = base+"ls_map"
    pixel_area = base+"pixel_area"
    pixel_area2 = base+"pixel_area2"
    offs = base+"offs"
    coffs = base+"coffs"
    coffsets = base+"coffsets"
    snr = base+"snr"
    ellipse_pixel_area = base+"ellipse_pixel_area"
    ratio_sigma0 = base+"ratio_sigma0"

    # read image parameter file for meta information
    par = ReadPar(master+".par")

    incidence = str(int(float(par.incidence_angle)))

    outname_base = outname_base+"_"+incidence

    ######################################################################
    # colelct srtm file sand mosaic them

    # define a name for the output mosaic
    name_srtm = os.path.join(tempdir, "srtm")

    # collect srtm tiles (if tiles are not found in the defined srtm directory, they are automatically downloaded to the temporary directory)
    targets = srtm.hgt_collect([x+".par" for x in files_mli], tempdir, demdir=srtmdir)

    print "preparing SRTM data..."
    srtm.mosaic(targets, name_srtm)

    # interpolate data gaps
    srtm.fill(name_srtm, name_srtm+"_fill", path_log, replace=True)
    name_srtm += "_fill"

    # project DEM to UTM
    if transform:
        srtm.transform(name_srtm, name_srtm+"_utm")
        name_srtm += "_utm"
    ######################################################################
    # create DEM products
    print "sar image simulation..."
    try:
        run(["gc_map", master+".par", "-", name_srtm+".par", name_srtm, dem_seg+".par", dem_seg, lut, dem_ovs, dem_ovs, sim_sar, u, v, inc, psi, pix, ls_map, 8, func_interp], logpath=path_log)
    except IOError:
        print "...failed"
        return

    ######################################################################
    print "initial pixel area estimation..."
    run(["pixel_area", master+".par", dem_seg+".par", dem_seg, lut, ls_map, inc, pixel_area], logpath=path_log)

    ######################################################################
    print "exact offset estimation..."
    try:
        inlist = ["", "0 0", "100 100", "128 128", 7.0]
        run(["create_diff_par", master+".par", "-", master+"_diff.par", 1], inlist=inlist, logpath=path_log)
        run(["offset_pwrm", master, pixel_area, master+"_diff.par", offs, snr, 128, 128, offs+".txt", "-", 200, 200, 7.0], logpath=path_log)
    except:
        print "...failed"
        return

    ######################################################################
    print "computation of offset polynomials..."
    try:
        run(["offset_fitm", offs, snr, master+"_diff.par", coffs, coffsets, "-", 4, 0], logpath=path_log)
    except:
        print "...failed"
        return

    ######################################################################
    print "supplementing lookuptable with offset polynomials..."
    try:
        sim_width = ReadPar(dem_seg+".par").width
        run(["gc_map_fine", lut, sim_width, master+"_diff.par", lut_fine, 0], logpath=path_log)
    except:
        print "...failed"
        return

    ######################################################################
    print "refined pixel area estimation..."
    try:
        run(["pixel_area", master+".par", dem_seg+".par", dem_seg, lut_fine, ls_map, inc, pixel_area2], logpath=path_log)
    except:
        print "...failed"
        return

    ######################################################################
    print "radiometric calibration and normalization..."
    try:
        slc_width = ReadPar(master+".par").range_samples
        run(["radcal_MLI", master, master+".par", "-", master+"_cal", "-", 0, 0, 1, 0.0, "-", ellipse_pixel_area], logpath=path_log)
        run(["ratio", ellipse_pixel_area, pixel_area2, ratio_sigma0, slc_width, 1, 1], logpath=path_log)
        for item in files_mli:
            run(["product", item, ratio_sigma0, item+"_pixcal", slc_width, 1, 1], logpath=path_log)
    except:
        print "...failed"
        return
    ######################################################################
    print "backward geocoding, normalization and conversion to dB..."
    for item in files_mli:
        run(["geocode_back", item+"_pixcal", slc_width, lut_fine, item+"_geo", sim_width, 0, func_geoback], logpath=path_log)

        run(["lin_comb", "1", item+"_geo", 0, math.cos(math.radians(float(par.incidence_angle))), item+"_geo_flat", sim_width], logpath=path_log)
        run(["sigma2gamma", item+"_geo_flat", inc, item+"_geo_norm", sim_width], logpath=path_log)

    ######################################################################

    print "creating final tiff files..."
    for item in finder(tempdir, ["*_geo_norm"]):
        polarization = re.findall("[HV]{2}", os.path.basename(item))[0].lower()
        outname = outname_base+"_"+polarization
        run(["data2geotiff", dem_seg+".par", item, 2, outname+"_geocoded_norm.tif"], logpath=path_log)
        annotation_dir = os.path.join(tempdir, "annotation")
        annotation = os.path.join(annotation_dir, [x for x in os.listdir(annotation_dir) if polarization in os.path.basename(x)][0])
        os.rename(annotation, outname+"_annotation.xml")

    ######################################################################
    print "cleaning up..."
    # copy, rename and edit quicklook kml and png
    shutil.copyfile(os.path.join(tempdir, "preview", "map-overlay.kml"), outname_base+"_quicklook.kml")
    shutil.copyfile(os.path.join(tempdir, "preview", "quick-look.png"), outname_base+"_quicklook.png")
    with open(outname_base+"_quicklook.kml", "r") as infile:
        kml = infile.read().replace("quick-look.png", os.path.basename(outname_base+"_quicklook.png"))
    with open(outname_base+"_quicklook.kml", "w") as outfile:
        outfile.write(kml)

    if not intermediates:
        shutil.rmtree(tempdir)

    if logfiles:
        os.rename(path_log, outname_base+"_log")

    print "...done:", asctime()
    print "##########################################"

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--transform", action="store_true", help="transform the final DEM to UTM coordinates")
    parser.add_argument("-l", "--logfiles", action="store_true", help="create logfiles of the executed GAMMA commands")
    parser.add_argument("-i", "--intermediates", action="store_true", help="keep intermediate files")
    parser.add_argument("zipfile", help="S1 zipped tempdir archive to be used")
    parser.add_argument("tempdir", help="temporary directory")
    parser.add_argument("outdir", help="output directory")
    parser.add_argument("srtmdir", help="directory containing SRTM hgt tiles (subdirectories possible)")
    args = parser.parse_args()

    main(args.zipfile, args.tempdir, args.outdir, args.srtmdir, args.transform, args.logfiles, args.intermediates)
