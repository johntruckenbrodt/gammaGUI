##############################################################
# Main GUI Interface                                         #
# John Truckenbrodt                                          #
##############################################################
import os

from ancillary import grouping, run, ReadPar

path_log = os.path.join(os.getcwd(), "LOG/LAT/")
if not os.path.exists(path_log):
    os.makedirs(path_log)

par = ReadPar(os.path.join(os.getcwd(), "PAR/circular.par"))

# create list of scene tuple objects
tuples = grouping()

print "#############################################"
print "transforming scenes..."

for scene in tuples:
    if len(set(["HH_slc","VV_slc", "HV_slc"]) & set(scene.__dict__.keys())) == 3:
        print scene.basename
        path_out = os.path.join(os.path.dirname(scene.HH_slc), "POL/")
        if not os.path.exists(path_out):
            os.makedirs(path_out)
        run(["lin_comb_cpx", "3", scene.HH_slc, scene.VV_slc, scene.HV_slc, par.constant_r, par.constant_i, par.factorHH_r, par.factorHH_i, par.factorVV_r, par.factorVV_i,
             par.factorHV_r, par.factorHV_i, scene.basename+"_rr", ReadPar(scene.HH_slc+".par").range_samples, "", "", par.pixav_x, par.pixav_y, "1"], path_out, path_log)
        run(["lin_comb_cpx", "3", scene.VV_slc, scene.HH_slc, scene.HV_slc, par.constant_r, par.constant_i, par.factorVV_r, par.factorVV_i, par.factorHH_r, par.factorHH_i,
             par.factorHV_r, par.factorHV_i, scene.basename+"_ll", ReadPar(scene.HH_slc+".par").range_samples, "", "", par.pixav_x, par.pixav_y, "1"], path_out, path_log)
        run(["lin_comb_cpx", "2", scene.HH_slc, scene.VV_slc, par.constant_r, par.constant_i, par.factorHH_r, par.factorHH_i, par.factorVV_r, par.factorVV_i,
             scene.basename+"_rl", ReadPar(scene.HH_slc+".par").range_samples, "", "", par.pixav_x, par.pixav_y, "1"], path_out, path_log)

print "...done"
print "#############################################"
