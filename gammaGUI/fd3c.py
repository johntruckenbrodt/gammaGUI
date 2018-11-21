##############################################################
# Target decomposition based on Freeman-Durden 3-component algorithm
# module of software gammaGUI
# John Truckenbrodt 2015
##############################################################
import os

from ancillary import grouping, run, finder, ReadPar, hdr

path_log = os.path.join(os.getcwd(), "LOG/LAT/")
if not os.path.exists(path_log):
    os.makedirs(path_log)

# create list of scene tuple objects
tuples = grouping()

print "#############################################"
print "creating fd3c decomposition..."

for scene in tuples:
    if len({"HH_slc_cal", "VV_slc_cal", "HV_slc_cal", "t13", "HH_slc_cal_mli"} & set(scene.__dict__.keys())) == 5:
        print scene.basename
        rlks = ReadPar(scene.HH_mli+".par").range_looks
        azlks = ReadPar(scene.HH_mli+".par").azimuth_looks
        run(["FD3C_DEC", scene.HH_slc, scene.HV_slc, scene.VV_slc, scene.t13, ReadPar(scene.HH_slc+".par").range_samples, scene.basename, rlks, azlks],
            os.path.dirname(scene.t13), path_log)
        for tag in ["_fdd_pd", "_fdd_ps", "_fdd_pv"]:
            hdr(scene.HH_mli+".par", os.path.join(os.path.dirname(scene.t13), scene.basename)+tag+".hdr")
# rename files to consistent pattern
for pattern in ["*.fdd*"]:
    for filename in finder(os.getcwd(), [pattern]):
        os.rename(filename, filename.replace(pattern.strip("*"), pattern.strip("*").replace(".", "_")))

print "...done"
print "#############################################"
