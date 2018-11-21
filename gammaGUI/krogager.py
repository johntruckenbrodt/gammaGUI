##############################################################
# Calculate Helix and Diplane composition from RR and LL circular components
# Multilook RL circular component (Sphere component)
# Sphere, Helix and Diplane represent the Krogager decomposition
# John Truckenbrodt
##############################################################

import os

from ancillary import grouping, run, ReadPar, hdr

path_log = os.path.join(os.getcwd(), "LOG/LAT/")

# create list of scene tuple objects
tuples = grouping()

print "#############################################"
print "creating krogager decomposition..."

for scene in tuples:
    if len(set(["HH_slc", "rl", "ll", "rr", "HH_mli"]) & set(scene.__dict__.keys())) == 5:
        print scene.basename
        path_out = os.path.dirname(scene.rl)
        mlipar = scene.HH_mli+".par"
        rlks = ReadPar(mlipar).range_looks
        azlks = ReadPar(mlipar).azimuth_looks
        run(["multi_look", scene.rl, scene.HH_slc+".par", scene.basename+"_sphere", mlipar, rlks, azlks], path_out, path_log)
        run(["diplane_helix", scene.ll, scene.rr, scene.HH_slc+".par", scene.basename+"_diplane", scene.basename+"_helix", mlipar, rlks, azlks, "-", "-", "-"], path_out, path_log)

        for tag in ["_sphere", "_helix", "_diplane"]:
            hdr(scene.HH_mli+".par", os.path.join(path_out, scene.basename)+tag+".hdr")

print "...done"
print "#############################################"