#!/usr/bin/env python2.7
import sys

import subprocess as sp
import multiprocessing as mp

from ancillary import finder

script = "/homes4/geoinf/ve39vem/scripts/python/S1_main.py"
zipdir = "/homes4/geoinf/ve39vem/RADAR/Sentinel/archive/sweden"
tempdir = "/homes4/geoinf/ve39vem/RADAR/Sentinel/test_in"
outdir = "/homes4/geoinf/ve39vem/RADAR/Sentinel/test_out"
srtmdir = "/geonfs02_vol1/SRTM_3_HGT/01_hgt"

def execute(item):
    # logfile = os.path.join(tempdir, os.path.basename(item)[:-4])
    sp.check_call([sys.executable, script, "-l", "-i", item, tempdir, outdir, srtmdir])


if __name__ == '__main__':

    files = finder(zipdir, ["*.zip"])

    files = [x for x in files if "GRDH" in x]

    pool = mp.Pool(processes=3)
    try:
        result = pool.map(execute, files)
    except:
        pool.close()
        pool.join()
