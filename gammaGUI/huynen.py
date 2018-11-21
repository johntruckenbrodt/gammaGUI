##############################################################
# Huynen decomposition to generate equivalent single target coherency matrix values
# John Truckenbrodt
##############################################################

import os

from ancillary import grouping, run, finder, ReadPar, union

path_log = os.path.join(os.getcwd(), "LOG/LAT/")
if not os.path.exists(path_log):
    os.makedirs(path_log)

# create list of scene tuple objects
tuples = grouping()

print "#############################################"
print "creating huynen decomposition..."
counter = 0
for scene in tuples:
    if len(union(["HH_slc", "VV_slc", "HV_slc", "t11", "t12", "t13"], scene.__dict__.keys())) == 6:
        print scene.basename
        for i in range(1, 4):
            run(["HUYNEN_DEC", scene.HH_slc, scene.HV_slc, scene.VV_slc, scene.t11, scene.t12, scene.t13, ReadPar(scene.HH_slc+".par").range_samples, scene.basename, str(i)],
                os.path.dirname(scene.t11), path_log)
        counter += 1
if counter == 0:
    print "no appropriate scenes with existing coherence matrix found"
else:
    # rename files to consistent pattern
    for pattern in ["*.t*", "*.im", "*.re"]:
        for filename in finder(os.getcwd(), [pattern]):
            os.rename(filename, filename.replace(pattern.strip("*"), pattern.strip("*").replace(".", "_")))

print "...done"
print "#############################################"