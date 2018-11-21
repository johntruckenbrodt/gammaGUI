##############################################################
# Kennaugh matrix derivation from scattering matrix elements
# module of software gammaGUI
# John Truckenbrodt 2015
##############################################################
import os

from ancillary import grouping, dissolve

path_log = os.path.join(os.getcwd(), "LOG/LAT/")
if not os.path.exists(path_log):
    os.makedirs(path_log)

# create list of scene tuple objects
tuples = grouping()

print "#############################################"
print "creating kennaugh decomposition..."

for scene in tuples:
    print scene.main
    items = [getattr(scene, x) if hasattr(scene, x) else "-" for x in ["t11", "t22", "t33", "t12", "t13", "t23"]]
    cmd = dissolve(["KENNAUGH_MATRIX", items, os.path.join(scene.main, scene.basename)])
    print cmd

print "...done"
print "#############################################"