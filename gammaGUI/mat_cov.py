##############################################################
# Calculate covariance matrix C elements from HH, HV, and VV SLC data
# module of software gammaGUI
# John Truckenbrodt 2015
##############################################################

import os

from ancillary import grouping, run, finder, ReadPar

path_log = os.path.join(os.getcwd(), "LOG/LAT/")
if not os.path.exists(path_log):
    os.makedirs(path_log)

par = ReadPar(os.path.join(os.getcwd(), "PAR/mat_cov.par"))

# create list of scene tuple objects
tuples = grouping()

print "#############################################"
print "creating covariance matrices..."

for scene in tuples:
    if len(set(["HH_slc", "VV_slc", "HV_slc", "HH_mli"]) & set(scene.__dict__.keys())) == 4:
        print scene.basename
        rlks = ReadPar(scene.HH_mli+".par").range_looks
        azlks = ReadPar(scene.HH_mli+".par").azimuth_looks
        path_out = os.path.join(os.path.dirname(scene.HH_slc), "POL/")
        if not os.path.exists(path_out):
            os.makedirs(path_out)
        run(["polcovar", scene.HH_slc, scene.HV_slc, scene.VV_slc, scene.HH_slc+".par", scene.HV_slc+".par", scene.VV_slc+".par", os.path.basename(scene.basename),
             os.path.basename(scene.basename)+"_mat_cov.par", rlks, azlks], path_out, path_log)

# rename files to consistent pattern
for filename in finder(os.getcwd(), ["*.c*"]):
    os.rename(filename, filename.replace(".c", "_c"))

print "...done"
print "#############################################"