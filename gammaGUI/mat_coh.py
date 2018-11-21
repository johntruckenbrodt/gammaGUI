##############################################################
# Calculate coherence matrix T elements from Pauli decomposition alpha, beta, gamma
# module of software gammaGUI
# John Truckenbrodt 2015
##############################################################
import os

from ancillary import grouping, run, finder, ReadPar

path_log = os.path.join(os.getcwd(), "LOG/LAT/")
if not os.path.exists(path_log):
    os.makedirs(path_log)

par = ReadPar(os.path.join(os.getcwd(), "PAR/mat_coh.par"))

tuples = grouping()

print "#############################################"
print "creating coherence matrices..."

for scene in tuples:
    if len(set(["pauli_alpha_slc", "pauli_beta_slc", "pauli_gamma_slc", "HH_mli"]) & set(scene.__dict__.keys())) == 4:
        print scene.basename
        rlks = ReadPar(scene.HH_mli+".par").range_looks
        azlks = ReadPar(scene.HH_mli+".par").azimuth_looks
        run(["polcoh", scene.pauli_alpha_slc, scene.pauli_beta_slc, scene.pauli_gamma_slc, scene.pauli_alpha_slc+".par", scene.pauli_beta_slc+".par", scene.pauli_gamma_slc+".par",
             scene.basename, scene.basename+"_mat_coh.par", rlks, azlks], os.path.dirname(scene.pauli_alpha_slc), path_log)

# rename files to consistent pattern
for filename in finder(os.getcwd(), ["*.t*"]):
    os.rename(filename, filename.replace(".t", "_t"))

print "...done"
print "#############################################"