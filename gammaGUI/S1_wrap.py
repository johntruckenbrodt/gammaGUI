import subprocess as sp
import sys
from ancillary import finder

script = "/pvdata2/john/GAMMA/gammaGUI/S1_main.py"
zipdir = "/pvdata2/john/RADAR/Sentinel/originals"
tempdir = "/pvdata2/john/RADAR/Sentinel/test"
outdir = "/pvdata2/john/RADAR/Sentinel/test_out"
srtmdir = "/pvdata2/john/RADAR/Sentinel/srtm"

files = finder(zipdir, ["*.zip"])

for scene in files:
    if "GRDH" in scene:
        sp.check_call([sys.executable, script, "-l", "-i", scene, tempdir, outdir, srtmdir])
