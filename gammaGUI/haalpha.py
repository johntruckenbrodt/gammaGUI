##############################################################
# Calculate H/A/alpha (Entropy, Anisotropy, and alpha) decomposition from the 3D Pauli feature vector
# John Truckenbrodt
##############################################################

import os

from ancillary import grouping, run, ReadPar, hdr

path_log = os.path.join(os.getcwd(), "LOG/LAT/")

# create list of scene tuple objects
tuples = grouping()

print "#############################################"
print "creating entropy-anisotropy-alpha decomposition..."

for scene in tuples:
    if len(set(["pauli_alpha_slc", "pauli_beta_slc", "pauli_gamma_slc", "HH_slc", "HH_mli"]) & set(scene.__dict__.keys())) == 5:
        print scene.basename
        path_out = os.path.dirname(scene.pauli_alpha_slc)
        mlipar = scene.HH_mli+".par"
        rlks = ReadPar(mlipar).range_looks
        azlks = ReadPar(mlipar).azimuth_looks
        run(["haalpha", scene.pauli_alpha_slc, scene.pauli_beta_slc, scene.pauli_gamma_slc, scene.HH_slc+".par", scene.basename+"_cpd_A", scene.basename+"_cpd_alpha",
             scene.basename+"_cpd_H", scene.basename+"_cpd_l1", scene.basename+"_cpd_l2", scene.basename+"_cpd_l3", mlipar, rlks, azlks], path_out, path_log)
        for tag in ["_cpd_A", "_cpd_alpha", "_cpd_H"]:
            hdr(scene.HH_mli+".par", os.path.join(path_out, scene.basename)+tag+".hdr")

print "...done"
print "#############################################"
