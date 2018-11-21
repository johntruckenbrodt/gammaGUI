##############################################################
# ERS-1/2-specific SLC data import and calibration
# module of software gammaGUI
# John Truckenbrodt 2015
##############################################################

"""
The following tasks are performed by executing this script:
-scan the defined import directory for the ERS-specific leader file LEA_01.001
-convert the data to gamma format
-create scene folders and rename the newly created files based on the sensor, frame id and acquisition time stamp
-scan the leader file for meta information relevant for calibration
-select a antenna gain correction lookup file from the extracted information; the files are stored in a subfolder CAL of this software package
-calibrate the SLC files based on the extracted meta information
-remove the uncalibrated SLCs
"""

import sys
import time
from math import log

import os
import re

from ancillary import finder, run, ReadPar

orbit_correct = True if sys.argv[-1] == "True" else False

# path to delft orbit files
path_delft = "/pvdata2/john/ancillary/ERS/ORBIT/delft"

# path to antenna correction files
path_cal = "/pvdata2/john/ancillary/ERS/CAL/ERS_antenna"

# define (and create) directory for logfile
path_log = os.path.join(os.getcwd(), "LOG/IMP/")
if not os.path.exists(path_log):
    os.makedirs(path_log)

scenes = [os.path.dirname(x) for x in finder(sys.argv[1], ["*LEA_01.001"])]

if len(scenes) == 0:
    raise IOError("no appropriate file found")

for scene in scenes:
    print "----------"
    # read leader file for meta information
    with open(os.path.join(scene, "LEA_01.001"), "r") as infile:
        text = [line for line in infile]
    text = "".join(text)

    # extract frame id
    frame_index = re.search("FRAME=", text).end()
    frame = text[frame_index:frame_index+4]

    tempname = os.path.join(os.getcwd(), "temp")
    print "importing..."
    run(["par_ESA_ERS", "LEA_01.001", tempname+".par", "DAT_01.001", tempname], scene, path_log, [""])
    par = ReadPar(tempname+".par")

    date = "".join([format(int(x), "02d") for x in par.date[0:3]])
    timestamp = date+"T"+time.strftime("%H%M%S", time.gmtime(round(float(par.center_time[0]))))
    outname = par.sensor+"_"+frame+"_"+timestamp+"_VV_slc"
    path_out = os.path.join(os.getcwd(), outname[:-7])
    if not os.path.exists(path_out):
        print outname
        os.makedirs(path_out)
        os.rename(tempname, os.path.join(path_out, outname))
        os.rename(tempname+".par", os.path.join(path_out, outname+".par"))
    else:
        print "scene", outname, "already imported; removing temporary files"
        os.remove(tempname)
        os.remove(tempname+".par")
    outname = os.path.join(path_out, outname)

    ###############################
    # extract calibration meta information
    # sensor = text[(720+395):(720+411)].strip(" \t\r\n\0")
    date = float(text[(720+67):(720+99)].strip(" \t\r\n\0")[:8])
    proc_fac = text[(720+1045):(720+1061)].strip(" \t\r\n\0")
    proc_sys = text[(720+1061):(720+1069)].strip(" \t\r\n\0")
    proc_vrs = text[(720+1069):(720+1077)].strip(" \t\r\n\0")

    text_subset = text[re.search("FACILITY RELATED DATA RECORD \[ESA GENERAL TYPE\]", text).start()-13:]
    cal = str(-10*log(float(text_subset[663:679].strip(" \t\r\n\0")), 10))
    antenna_flag = text_subset[659:663].strip(" \t\r\n\0")

    # the following section is only relevant for PRI products and can be considered future work
    # select antenna gain correction lookup file from extracted meta information
    # the lookup files are stored in a subfolder CAL which is included in the gammaGUI software package
    # if sensor == "ERS1":
    #     if date < 19950717:
    #         antenna = "antenna_ERS1_x_x_19950716"
    #     else:
    #         if proc_sys == "VMP":
    #             antenna = "antenna_ERS2_VMP_v68_x" if proc_vrs >= 6.8 else "antenna_ERS2_VMP_x_v67"
    #         elif proc_fac == "UKPAF" and date < 19970121:
    #             antenna = "antenna_ERS1_UKPAF_19950717_19970120"
    #         else:
    #             antenna = "antenna_ERS1"
    # else:
    #     if proc_sys == "VMP":
    #         antenna = "antenna_ERS2_VMP_v68_x" if proc_vrs >= 6.8 else "antenna_ERS2_VMP_x_v67"
    #     elif proc_fac == "UKPAF" and date < 19970121:
    #         antenna = "antenna_ERS2_UKPAF_x_19970120"
    #     else:
    #         antenna = "antenna_ERS2"

    antenna = "antenna_"+par.sensor

    print "sensor:", par.sensor
    print "date:", int(date)
    print "processing facility:", proc_fac
    print "processing system:", proc_sys
    print "processing version:", proc_vrs
    print "antenna correction flag:", antenna_flag
    print "antenna correction file:", antenna
    print "calibration constant K [dB]:", cal

    sc_db = "59.61" if par.sensor == "ERS1" else "60"
    antenna_corr = "1" if antenna_flag == "0" else "0"
    antenna = os.path.join(path_cal, antenna)

    if orbit_correct:
        print "...correcting orbits"
        try:
            if par.sensor == "ERS1":
                path_delft_target = os.path.join(path_delft, par.sensor, "dgm-e04" if int(date) <= 19960601 else "dgm-e04.fd")
            else:
                path_delft_target = os.path.join(path_delft, par.sensor, "dgm-e04")
            run(["DELFT_vec2", outname+".par", path_delft_target], path_out, path_log)
        except:
            pass

    # perform radiometric calibration
    print "...calibrating"
    run(["radcal_SLC", outname, outname+".par", outname+"_cal", outname+"_cal.par", "4", antenna, "1", antenna_corr, "1", sc_db, cal], path_out, path_log)

    os.remove(os.path.join(path_out, outname))
    os.remove(os.path.join(path_out, outname)+".par")
