##############################################################
# Cloude target decomposition from elements of scattering and coherency matrix
# module of software gammaGUI
# John Truckenbrodt 2015
##############################################################

import os

from ancillary import grouping, run, finder, ReadPar, hdr

path_log = os.path.join(os.getcwd(), "LOG/LAT/")
if not os.path.exists(path_log):
    os.makedirs(path_log)

par = ReadPar(os.path.join(os.getcwd(), "PAR/cloude.par"))

# create list of scene tuple objects
tuples = grouping()

print "#############################################"
print "creating cloude decomposition..."

counter = 0

for scene in tuples:
    if len({"HH_slc", "VV_slc", "HV_slc", "t12", "t13", "HH_mli"} & set(scene.__dict__.keys())) == 6:
        counter += 1
        print scene.basename
        rlks = ReadPar(scene.HH_mli+".par").range_looks
        azlks = ReadPar(scene.HH_mli+".par").azimuth_looks
        run(["CLOUDE_DEC", scene.HH_slc, scene.HV_slc, scene.VV_slc, scene.t12, scene.t13, ReadPar(scene.HH_slc+".par").range_samples, scene.basename, rlks,
             azlks], os.path.dirname(scene.t12), path_log)
        # create envi header files (note: number of lines must be reduced by 1 on import into envi)
        for i in range(1, 4):
            hdr(scene.HH_mli+".par", os.path.join(os.path.dirname(scene.t12), scene.basename)+"_ctd_"+str(i)+"_mag.hdr")

if counter == 0:
    print "no scenes with required scattering and coherency matrix elements found"

# rename files to consistent pattern
for pattern in ["*.ctd*", "*.mag", "*.pha"]:
    for filename in finder(os.getcwd(), [pattern]):
        os.rename(filename, filename.replace(pattern.strip("*"), pattern.strip("*").replace(".", "_")))

print "...done"
print "#############################################"
