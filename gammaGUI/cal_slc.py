import os

from ancillary import finder, ReadPar, run



# read parameter file
par = ReadPar(os.path.join(os.getcwd(), "PAR/cal_slc.par"))

# define (and create) directories for processing results and logfile
path_log = os.path.join(os.getcwd(), "LOG/GEO/")
path_out = os.path.join(os.getcwd(), "ISP/")
for path in [path_log, path_out]:
    if not os.path.exists(path):
        os.makedirs(path)

list_K_dB = {"PSR1": "-115.0"}

list_slc = finder(os.getcwd(), ["*_slc"])

if len(list_slc) > 0:
    print "#############################################"
    print "calibration started..."

    for name_slc in list_slc:
        sensor = name_slc.split("_")[0]
        if sensor in list_K_dB:
            K_dB = list_K_dB[sensor]
        else:
            print "calibration for sensor "+sensor+"not implemented"

        name_cslc = name_slc[:-3]+"cslc"

        run(["radcal_SLC", name_slc, name_slc+".par", name_cslc, name_cslc+".par", "1", "-", "0", "0", "0", "0", "-", K_dB], path_out, path_log)

    print "...done"
    print "#############################################"
else:
    print "#############################################"
    print "no SLCs found"
    print "#############################################"