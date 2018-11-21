##############################################################
# Calculate Pauli polarimetric decomposition from HH, VV, and HV SLC images
# John Truckenbrodt 2015
##############################################################

import os

from ancillary import grouping, run, finder

path_log = os.path.join(os.getcwd(), "LOG/LAT/")
if not os.path.exists(path_log):
    os.makedirs(path_log)

# create list of scene tuple objects
# all images following the defined patterns within the same folder (i.e. the same acquisition) will be grouped together
tuples = grouping()

print "#############################################"
print "creating pauli decomposition..."

for scene in tuples:
    if len(set(["HH_slc", "VV_slc", "HV_slc"]) & set(scene.__dict__.keys())) == 3:
        print scene.basename
        path_out = os.path.join(os.path.dirname(scene.HH_slc), "POL/")
        if not os.path.exists(path_out):
            os.makedirs(path_out)
        name_out = os.path.join(path_out, os.path.basename(scene.HH_slc)[:-6]+"pauli")
        run(["pauli", scene.HH_slc, scene.VV_slc, scene.HV_slc, scene.HH_slc+".par", scene.VV_slc+".par", scene.HV_slc+".par", name_out], os.getcwd(), path_log)

# rename files to consistent pattern
for filename in finder(os.getcwd(), ["*.slc*"]):
    os.rename(filename, filename.replace(".slc", "_slc"))

print "...done"
print "#############################################"