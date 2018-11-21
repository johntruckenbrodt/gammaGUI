##############################################################
# SLC coregistration
# module of software gammaGUI
# John Truckenbrodt, Soner Uereyen 2015
##############################################################

"""
The following tasks are performed by executing this script:
-reading of a parameter file coreg.par (in subfolder PAR of GUI working directory)
--see object par for necessary values; file is automatically created by starting the script via the GUI
-if necessary, creation of output and logfile directories
-creating the offset parameter file
-estimation of initial range and azimuth offsets
-precise estimation of offset polynomials
-generation of offsets polynomials
-resampling of slc file
"""

import sys

import os

from isp_parameterfile import ISPPar
from ancillary import ReadPar, run, Spacing


# retrieve additional arguments
slc1 = sys.argv[1]
slc2 = sys.argv[2]

# read processing parameter textfile
par = ReadPar(os.path.join(os.getcwd(), "PAR/coreg.par"))

# set SNR theshold (this should not be changed)
thres = 7.0

# define (and create) directories for processing results and logfile
path_log = os.path.join(os.getcwd(), "LOG/ISP/")
path_out = os.path.join(os.getcwd(), "ISP/")
for path in [path_log, path_out]:
    if not os.path.exists(path):
        os.makedirs(path)

# concatenate output names
name_base = os.path.basename(slc1)+"_"+os.path.basename(slc2)+"_"
name_coffs = name_base + "coffs"
name_coffsets = name_base + "coffsets"
name_off = name_base + "off"
name_offs = name_base + "offs"
name_offsets = name_base + "offsets"
name_snr = name_base + "snr"
name_reg = name_base + "reg"

print "#############################################"
print os.path.basename(slc1), "->", os.path.basename(slc2)
print "----------"
print "coregistration started..."

run(["create_offset", slc1 + ".par", slc2 + ".par", name_off, par.algorithm, 1, 1, 0], path_out, path_log)

print "...estimation of initial range and azimuth offsets"

# first estimation using orbit data (most important in case of very large offsets)
run(["init_offset_orbit", slc1 + ".par", slc2 + ".par", name_off], path_out, path_log)

# repeated offset estimation using different levels of multilooking
isp = ReadPar(slc1 + ".par")
mlk = Spacing(isp)

for factor in [4, 2, 1]:
    run(["init_offset", slc1, slc2, slc1 + ".par", slc2 + ".par", name_off, str(int(mlk.rlks)*factor), str(int(mlk.azlks)*factor), "-", "-", "-", "-", thres], path_out, path_log)
run(["init_offset", slc1, slc2, slc1 + ".par", slc2 + ".par", name_off, 1, 1, "-", "-", "-", "-", thres], path_out, path_log)

# compute the number of estimation windows in azimuth from the defined number of range windows
dim_ratio = float(isp.azimuth_lines)/float(isp.range_samples)
naz = str(int(int(par.nr)*dim_ratio))

print "...cross-correlation offset and polynomial estimation"
run(["offset_pwr", slc1, slc2, slc1+".par", slc2+".par", name_off, name_offs, name_snr, par.rwin, par.azwin, name_offsets, par.n_ovr, par.nr, naz, thres], path_out, path_log)
run(["offset_fit", name_offs, name_snr, name_off, name_coffs, name_coffsets, thres, par.npoly], path_out, path_log)
rwin_2 = str(int(par.rwin)/2)
azwin_2 = str(int(par.azwin)/2)
nr_2 = str(int(par.nr)*2)
naz_2 = str(int(naz)*2)
run(["offset_pwr", slc1, slc2, slc1+".par", slc2+".par", name_off, name_offs, name_snr, rwin_2, azwin_2, name_offsets, par.n_ovr, nr_2, naz_2, thres], path_out, path_log)
run(["offset_fit", name_offs, name_snr, name_off, name_coffs, name_coffsets, thres, par.npoly], path_out, path_log)

print "...resampling of SLC file"
run(["SLC_interp", slc2, slc1 + ".par", slc2 + ".par", name_off, name_reg, name_reg+".par"], path_out, path_log)

print "...done"
print "#############################################"
