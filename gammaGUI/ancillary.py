##############################################################
# core routines for software gammaGUI
# John Truckenbrodt 2014-2015
##############################################################
"""
This script gathers central functions and object instances for processing SAR images using the software GAMMA within the GUI
Please refer to the descriptions of the individual functions/instances for details
"""

import os
import re
import math
import shutil
import osr
import tkMessageBox
from Tkinter import *
from glob import glob
import subprocess as sp


# wrapper for batch-processing
def batch(args, tags_search, tag_exclude):
    # find processing candidates
    candidates = finder(Environment.workdir.get(), tags_search)
    for item in candidates:
        items = list(args)
        items.append(item)
        # check whether processing results already exist and execute command if they do not
        if not os.path.isfile(item+tag_exclude):
            sp.check_call(items, cwd=Environment.workdir.get())


# convert between epsg, wkt and proj4 spatial references
def crsConvert(crsText, crsOut):
    srs = osr.SpatialReference()
    try:
        check = srs.ImportFromEPSG(crsText)
        if check != 0:
            raise IOError
    except:
        try:
            check = srs.ImportFromWkt(crsText)
            if check != 0:
                raise IOError
        except:
            try:
                check = srs.ImportFromProj4(crsText)
                if check != 0:
                    raise IOError
            except:
                print "input type not supported; must be either epsg, wkt or proj4"
    if crsOut == "wkt":
        return srs.ExportToWkt()
    elif crsOut == "proj4":
        return srs.ExportToProj4()
    elif crsOut == "epsg":
        return int(srs.GetAttrValue("AUTHORITY", 1))


# list and tuple flattening
def dissolve(inlist):
    out = []
    for i in inlist:
        i = list(i) if type(i) is tuple else i
        out.extend(dissolve(i)) if type(i) is list else out.append(i)
    return out


# gui design and structure dictionaries
class Environment(object):

    # place holder for the later defined working directory
    workdir = ""

    # general GUI design specifications
    bcolor = {"bg": 'black'}
    label_ops = {"bg": "black", "fg": "white", "font": ("system", 10, "bold")}
    header_ops = {"bg": "black", "fg": "white", "font": ("system", 12, "bold"), "pady": 5}
    menu_ops = {"bg": "black", "fg": "white", "font": ("system", 10, "bold"), "activebackground": "white", "activeforeground": "black", "bd": 2}
    button_ops = {"bg": "white", "fg": "black", "font": ("system", 10, "bold"), "activebackground": "black",
                  "activeforeground": "white", "highlightbackground": "white"}
    checkbutton_ops = {"bg": "black", "fg": "black", "font": ("system", 10, "bold"), "activebackground": "black", "width": 21, "height": 1, "bd": .5,
                  "activeforeground": "black", "highlightbackground": "black"}

    # define extra text printed in the dialog window
    args_extra = {"multilooking": "Compute MLIs from all SLCs in all subdirectories",
                  "cc_ad": "estimate coherence from all generated interferograms",
                  "cc_wave": "estimate coherence from all generated interferograms",
                  "interferogram flattening": "flatten all existing interferograms",
                  "srtm download": "download SRTM tiles covering all existing SLCs",
                  "geocoding": "geocode and topo-normalize all MLI, coherence and decomposition images",
                  "SLC calibration": "calibrate all existing SLCs",
                  "SLC coregistration (batched)": "batched coregistration with a tab-separated two-column file list",
                  "export/delete files": "remove files matching a pattern or copy them to a subdirectory EXP",
                  "temporal filtering": "temporal filtering of all intensity images and polarimetric decompositions"}

    # path (relative to working directory) and name of parameter files for specified commands
    parnames = {"baseline estimation": "/PAR/baseline.par",
                "cc_ad": "/PAR/coherence_ad.par",
                "cc_wave": "/PAR/coherence_wave.par",
                "dem preparation": "/PAR/dem.par",
                "geocoding": "/PAR/scene.par",
                "interferogram flattening": "/PAR/ph_slope_base.par",
                "interferogram generation": "/PAR/interferogram.par",
                "kml generation": "/PAR/kml.par",
                "SLC coregistration": "/PAR/coreg.par"}

    # dropdown button lookup and options
    dropoptions = {"str": ["method flag", "mode", "resampling method", "sensor"],
                   "int": ["wgt_ad", "wgt_wave", "wgt_tfilt"],
                   "method flag": ["0", "1", "2", "3", "4"],
                   "mode": ["export", "delete"],
                   "resampling method": ["near", "bilinear", "cubic", "cubicspline", "lanczos", "average", "mode", "max", "min", "med", "q1", "q3"],
                   "sensor": ["All", "PSR1", "PSR2", "CSK", "S1", "TDX", "TSX", "RS2"],
                   "wgt_ad": ["constant", "gaussian"],
                   "wgt_wave": ["constant", "triangular", "gaussian", "none (phase only)"],
                   "wgt_tfilt": ["uniform", "linear", "gaussian"]}

    # check button lookup table
    checkbuttons = ["topographic normalization", "regexp", "deramp (S1 SLC only)", "mosaic (S1 SLC only)", "orbit correction", "differential", "utm"]


# execute child window command
def execute(action, fileList, arguments):

    text = []
    if len(action) > 1:
        if ".py" in action[1]:
            # add path to name of script
            action[1] = os.path.join(os.getcwd(), action[1])
    # list all necessary arguments
    for arg in action:
        text.append(arg)

    for obj in fileList:
        text.append(obj.file.get())

    if len(action) > 1:
        if "srtm_preparation.py" in action[1]:
            arguments.append(["SRTM_archive", fileList[0].file])

    # evaluate processing parameters
    for i in range(0, len(arguments)):
        if arguments[i][0] in Environment.dropoptions["int"]:
            arguments[i][1] = str(Environment.dropoptions[arguments[i][0]].index(arguments[i][1].get()))
        else:
            try:
                arguments[i][1] = arguments[i][1].get()
            except:
                pass

        if arguments[i][1] != "SRTM_archive":
            text.append(arguments[i][1])


    # execute subprocess (GAMMA) commands
    try:
        if len(action) > 1:
            path_par = os.path.join(Environment.workdir.get(), "PAR/")
            if not os.path.exists(path_par):
                os.makedirs(path_par)
            basename_script = "coreg" if "coreg" in action[1] else os.path.splitext(os.path.basename(action[1]))[0]
            writer(path_par+basename_script+".par", arguments, strfill=False)
            if os.path.basename(action[1]) == "reader.py":
                print "#############################################"
                print "importing files..."
                importer(text)
                print "...done"
                print "#############################################"
            elif os.path.basename(action[1]) == "multilook.py":
                print "#############################################"
                print "multilooking files..."
                batch(text, ["*_slc", "*_slc_cal", "*_slc_reg", "*_slc_cal_reg"], "_mli")
                print "...done"
                print "#############################################"
            elif os.path.basename(action[1]) == "srtm_preparation.py":
                sp.check_call(text[:2], cwd=Environment.workdir.get())
            else:
                sp.check_call(text, cwd=Environment.workdir.get())

        elif "dis" in action[0]:
            if "dem_par" in action[0]:
                text.append(text[1]+".par")
            if "disrmg" in action[0]:
                if len(text[2]) == 0:
                    text[2] = "-"
                samples = ReadPar(finder(Environment.workdir.get(), [re.findall("[A-Z0-9_]{10}[0-9T]{15}_[HV]{2}_slc(?:_cal)?", text[1])[0]])[0]+".par").range_samples
                text.append(samples)

            elif "mph" in action[0]:
                samples = ReadPar(finder(Environment.workdir.get(), [re.findall("[A-Z0-9_]{10}[0-9T]{15}_[HV]{2}_slc(?:_cal)?", text[1])[0]])[0]+".par").range_samples
                text.append(samples)
                if "2" in action[0]:
                    samples = ReadPar(finder(Environment.workdir.get(), [re.findall("[A-Z0-9_]{10}[0-9T]{15}_[HV]{2}_slc(?:_cal)?", text[2])[0]])[0]+".par").range_samples
                    text.append(samples)
            else:
                for i in range(1, len(text)):
                    try:
                        text.append(ReadPar(text[i] + ".par").range_samples)
                    except:
                        continue
            print "#############################################"
            sp.check_call(text)
        if "dis" not in action[0]:
            tkMessageBox.showinfo("execution end", "processing successfully completed")
    except IOError:
        tkMessageBox.showerror("execution error", "incorrect or missing parameters")


# function for finding files in a folder and its subdirectories
# search patterns must be given in a list
# patterns can follow the unix shell standard (default) or regular expressions (via argument regex)
# the argument recursive decides whether search is done recursively in all subdirectories or in the defined directory only
# foldermodes:
# 0: no folders
# 1: folders included
# 2: only folders
def finder(folder, matchlist, foldermode=0, regex=False, recursive=True):
    # match patterns
    if regex:
        if recursive:
            out = dissolve([[os.path.join(group[0], x) for x in dissolve(group) if re.search(pattern, x)] for group in os.walk(folder) for pattern in matchlist])
        else:
            out = dissolve([[os.path.join(folder, x) for x in os.listdir(folder) if re.search(pattern, x)] for pattern in matchlist])
    else:
        if recursive:
            out = list(set([f for files in [glob(os.path.join(item[0], pattern)) for item in os.walk(folder) for pattern in matchlist] for f in files]))
        else:
            out = dissolve([glob(os.path.join(folder, pattern)) for pattern in matchlist])
    # exclude directories
    if foldermode == 0:
        out = [x for x in out if not os.path.isdir(x)]
    if foldermode == 2:
        out = [x for x in out if os.path.isdir(x)]
    return sorted(out)


# search working directory for scene folders and store image names into list of objects
def grouping(filepath=os.getcwd()):
    # list top level subfolders (i.e. no sub-subfolders) of the defined filepath if their names match the defined expression (i.e. sensor_timestamp)
    scenes = sorted([os.path.join(filepath, z) for z in os.listdir(filepath) if re.search("[0-9]{8}T[0-9]{6}", z)])
    scenes = finder(filepath, ["[0-9]{8}T[0-9]{6}"], regex=True, foldermode=2, recursive=False)
    # return list of scene objects
    return [Tuple(scene) for scene in scenes]


# write ENVI header files
def hdr(data, filename="same"):
    hdrobj = data if isinstance(data, HDRobject) else HDRobject(data)
    filename = hdrobj.filename[:-3]+"hdr" if filename is "same" else filename
    with open(filename, "w") as out:
        out.write("ENVI\n")
        for item in ["description", "samples", "lines", "bands", "header_offset", "file_type", "data_type", "interleave", "sensor_type", "byte_order", "map_info",
                     "coordinate_system_string", "wavelength_units", "band_names"]:
            if hasattr(hdrobj, item):
                value = getattr(hdrobj, item)
                if isinstance(value, list):
                    out.write(item.replace("_", " ") + " = {" + ", ".join([str(x) for x in value]) + "}\n")
                elif item in ["description", "band_names", "coordinate_system_string"]:
                    out.write(item.replace("_", " ") + " = {" + value + "}\n")
                else:
                    out.write(item.replace("_", " ") + " = " + str(value) + "\n")


# create ENVI hdr file object from existing .par or .hdr file
# for creating new headers from .par files currently only EQA and UTM projections with WGS-84 ellipsoid are supported
class HDRobject(object):
    def __init__(self, parfile="None"):
        self.filename = "None" if parfile == "None" else parfile
        if re.search(".hdr$", parfile):
            with open(parfile, "r") as infile:
                lines = infile.readlines()
                i = 0
                while i < len(lines):
                    line = lines[i].strip("\r\n")
                    if "=" in line:
                        if "{" in line and "}" not in line:
                            while "}" not in line:
                                i += 1
                                line += lines[i].strip("\n").lstrip()
                        line = filter(None, re.split("\s+=\s+", line))
                        line[1] = re.split(",[ ]*", line[1].strip("{}"))
                        setattr(self, line[0].replace(" ", "_"), line[1] if len(line[1]) > 1 else line[1][0])
                    i += 1
            if type(self.band_names) == str:
                self.band_names = [self.band_names]
        else:
            args = {"bands": 1,
                    "header_offset": 0,
                    "file_type": "ENVI Standard",
                    "interleave": "bsq",
                    "sensor_type": "Unknown",
                    "byte_order": 1,
                    "wavelength_units": "Unknown"}
            if parfile != "None":
                par = ReadPar(parfile)
                self.samples = getattr(par, union(["width", "range_samples", "samples"], par.__dict__.keys())[0])
                self.lines = getattr(par, union(["nlines", "azimuth_lines", "lines"], par.__dict__.keys())[0])
                for arg in args:
                    setattr(self, arg, args[arg])
                dtypes = {"FCOMPLEX": 6, "FLOAT": 4, "REAL*4": 4, "INTEGER*2": 2}
                self.data_type = dtypes[getattr(par, union(["data_format", "image_format"], par.__dict__.keys())[0])]
                if self.data_type == 6:
                    self.complex_function = "Power"
                # projections = ["AEAC", "EQA", "LCC", "LCC2", "OMCH", "PC", "PS", "SCH", "TM", "UTM"]
                if hasattr(par, "DEM_projection"):
                    if par.DEM_projection == "UTM":
                        hem = "North" if float(par.false_northing) == 0 else "South"
                        self.map_info = ["UTM", "1.0000", "1.0000",
                                         par.corner_east, par.corner_north,
                                         str(abs(float(par.post_east))), str(abs(float(par.post_north))),
                                         par.projection_zone, hem, "WGS-84", "units=Meters"]
                    elif par.DEM_projection == "EQA":
                        self.map_info = ["Geographic Lat/Lon", "1.0000", "1.0000",
                                         par.corner_lon, par.corner_lat,
                                         str(abs(float(par.post_lon))), str(abs(float(par.post_lat))),
                                         "WGS-84", "units=Degrees"]
                    else:
                        raise IOError("unsupported projection")
            else:
                self.samples = 0
                self.lines = 0
                for arg in args:
                    setattr(self, arg, args[arg])


# wrapper for file import
# imported files are first moved to a temporary directory
# folders are created with names based on information retrieved from the newly generated gamma parameter files
# files in the temporary directory are then moved to the newly created folder and the temporary folder removed
def importer(text):
    # set all files and folders of the input directory as possible import candidates
    candidates = finder(text[2], ["*"], foldermode=1)
    # create directories
    path_tmp = os.path.join(Environment.workdir.get(), "Temp")
    path_log = os.path.join(Environment.workdir.get(), "LOG/IMP")
    for path in [path_tmp, path_log]:
        if not os.path.exists(path):
            os.makedirs(path)
    # lists for storing coordinates of imported files
    latitudes = []
    longitudes = []

    for item in candidates:
        # reduce list to interpreter and scriptname
        args = list(text[:2])

        # if set, add sensor
        if text[3] != "All":
            args.append("-m")
            args.append(text[3])

        # add filename to list of execution arguments
        args.append("-s")
        args.append(item)

        # try to import file, if not possible (i.e. not an accepted format) continue with the next file
        try:
            run(args, path_tmp, path_log)
            # find next best parameter file of the newly imported files
            name_par = finder(path_tmp, ["*.par"])[0]

            print re.sub("w[0-9]__", "wx__", os.path.basename(name_par)[:25])

            # read parameter file
            par = ISPPar(name_par)

            # extract time stamp and sensor from parameter file name
            time = re.findall("[0-9]{8}T[0-9]{6}", name_par)[0]
            sensor = os.path.basename(name_par).split("_")[0]

            # define path for the imported files to be stored
            path_out = Environment.workdir.get() + "/" + sensor + "_" + time
            if not os.path.exists(path_out):
                os.makedirs(path_out)
            latitudes.append(par.center_latitude)
            longitudes.append(par.center_longitude)
            for x in finder(path_tmp, "*"):
                try:
                    shutil.move(x, path_out)
                except:
                    os.remove(x)
        except:
            continue
    os.rmdir(path_tmp)
    # give warning if lat/long differs by more than 1 degree
    # if max(longitudes) - min(longitudes) > 1 or max(latitudes) - min(latitudes) > 1:
    #     tkMessageBox.showwarning("working directory warning", "latitudes or longitudes differ by more than 1deg!")


class ISPPar(object):
    """Reader for ISP parameter files of the GAMMA software package.

    This class allows to read all information from filed in GAMMA's parameter file format. Each key-value pair is parsed
    and added as attributes. For instance if the parameter file contains the pair 'sensor:    TSX-1' a attribute named
    'sensor' with the value 'TSX-1' will be available.

    The values are converted to native Python types, while unit identifiers like 'dB' or 'Hz' are removed. Please see
    the GAMMA reference manual for further information on the actual file format.
    """

    _re_kv_pair = re.compile(r'^(\w+):\s*(.+)\s*')
    _re_float_literal = re.compile(r'^[+-]?(?:(?:\d*\.\d+)|(?:\d+\.?))(?:[Ee][+-]?\d+)?')

    def __init__(self, filename):
        """Parses a ISP parameter file from disk.

        Args:
            filename: The filename or file object representing the ISP parameter file.
        """
        if isinstance(filename, basestring):
            par_file = open(filename, 'r')
        else:
            par_file = filename
        try:
            par_file.readline()  # Skip header line
            for line in par_file:
                match = ISPPar._re_kv_pair.match(line)
                if not match:
                    continue  # Skip malformed lines with no key-value pairs
                key = match.group(1)
                items = match.group(2).split()
                if len(items) == 0:
                    value = None
                elif len(items) == 1:
                    value = ISPPar._parse_literal(items[0])
                else:
                    if not ISPPar._re_float_literal.match(items[0]):
                        # Value is a string literal containing whitespace characters
                        value = match.group(2)
                    else:
                        # Evaluate each item and stop at the first non-float literal
                        value = []
                        for i in items:
                            match = ISPPar._re_float_literal.match(i)
                            if match:
                                value.append(ISPPar._parse_literal(match.group()))
                            else:
                                # If the first float literal is immediately followed by a non-float literal handle the
                                # first one as singular value, e.g. in '20.0970 dB'
                                if len(value) == 1:
                                    value = value[0]
                                break
                setattr(self, key, value)
        finally:
            par_file.close()

    @staticmethod
    def _parse_literal(x):
        """Converts a object in either a integer, floating point or string literal.

        Utilizes the built-in conversion functions int, float and str to convert a arbitrary object. The functions are
        applied in that particular order.

        Args:
            x: Any object to be converted.

        Returns:
            The converted literal.
        """
        try:
            return int(x)
        except ValueError:
            try:
                return float(x)
            except ValueError:
                return str(x)


# Sentinel 1 deramping (not tested)
def s1_deramp(scenefolder, path_log):
    tops = finder(scenefolder, ["*.tops_par"])
    if len(tops) > 0:
        tab1 = os.path.join(scenefolder, "tab_deramp1")
        tab2 = os.path.join(scenefolder, "tab_deramp2")
        with open(tab1, 'w') as out:
            for item in tops:
                out.write(item[:-9]+"\t"+item[:-9]+".par"+"\t"+item+"\n")
        with open(tab2, 'w') as out:
            for item in tops:
                id_pt = re.search("_[ie]w[0-9]_", item)
                id = item[id_pt.start():id_pt.end()]
                id_out = id[1:4]+"dr"
                item = item.replace(item[id_pt.start():id_pt.end()], id_out)
                out.write(item[:-9]+"\t"+item[:-9]+".par"+"\t"+item+"\n")
        run(["SLC_deramp_S1_TOPS", tab1, tab2, "0", "0"], scenefolder, path_log)


# create an entry form for execution parameters
def makeform(self, fields, defaultentries):
    entries = []
    for i in range(0, len(fields)):
        row = Frame(self, Environment.bcolor)
        row.pack(side=TOP, padx=5, pady=5)
        lab = Label(row, Environment.label_ops, width=25, text=fields[i], anchor='w')
        lab.pack(side=LEFT)

        # add dropdown button
        if fields[i] in Environment.dropoptions:
            optionlist = Environment.dropoptions[fields[i]]
            var = StringVar(self)
            if fields[i] in Environment.dropoptions["int"]:
                default = Environment.dropoptions[fields[i]][int(defaultentries[i])]
            else:
                default = defaultentries[i]
            var.set(default)
            ent = OptionMenu(row, var, *optionlist)
            ent.pack(side=RIGHT, expand=YES)
            ent.config(Environment.button_ops, width=14, bd=.5)
            entries.append([fields[i], var])
        # add checkbutton
        elif fields[i] in Environment.checkbuttons:
            var = StringVar(self)
            var.set(str(defaultentries[i]))
            ent = Checkbutton(row, variable=var, onvalue="True", offvalue="False")
            ent.pack(side=RIGHT, expand=YES)
            ent.config(Environment.checkbutton_ops)
            entries.append([fields[i], var])
        # add text entry field
        else:
            ent = Entry(row)
            ent.pack(side=RIGHT, expand=YES)
            ent.insert(0, defaultentries[i])
            entries.append([fields[i], ent])
    return entries


# return the smallest possible data type
def parse_literal(x):
    try:
        return int(x)
    except ValueError:
        try:
            return float(x)
        except ValueError:
            return str(x)


# read processing parameter text files
class ReadPar(object):
    def __init__(self, filename, splits="[:|\t|=\s]", type=""):
        if type == "exe":
            splits = "[\t\n]"
        with open(filename, "r") as infile:
            self.index = []
            for line in infile:
                if not line.startswith("#"):
                    items = filter(None, re.split(splits, line))
                    if len(items) > 1:
                        if len(items) > 2:
                            entry = items[1] if items[2] in ["m", "decimal", "arc-sec", "degrees"] else items[1:]
                            if "".join(entry) == "WGS1984":
                                entry = "WGS84"
                        else:
                            entry = items[1]
                        if type == "exe":
                            items[0] = items[0].replace(" ", "_")
                        setattr(self, items[0], entry)
                        self.index.append(items[0])


# wrapper for subprocess execution including logfile writing and command prompt piping
def run(cmd, outdir=None, logpath=None, inlist=None):
    cmd = dissolve(cmd)
    cmd = [str(x) for x in cmd]
    if outdir is None:
        outdir = os.getcwd()
    if logpath is None:
        log = sp.PIPE
    else:
        if cmd[0] in [sys.executable, "Rscript"]:
            logfile = os.path.join(logpath, os.path.basename(cmd[1])[:-3]+".log")
        else:
            logfile = os.path.join(logpath, cmd[0]+".log")
        log = open(logfile, "a")
    if inlist is None:
        sp.check_call(cmd, stdout=log, cwd=outdir)
    else:
        sp.Popen(cmd, stdin=sp.PIPE, stdout=log, stderr=sp.PIPE, cwd=outdir, universal_newlines=True, shell=False).communicate("".join([str(x)+"\n" for x in inlist]))
    # add line for separating log entries of repeated function calls
    if logpath is not None:
        log.write("#####################################################################\n")
        log.close()


# compute ground multilooking factors and pixel spacings from an ISPPar object for a defined target resolution
class Spacing(object):
    def __init__(self, par, targetres="automatic"):
        # compute ground range pixel spacing
        par = par if isinstance(par, ReadPar) else ReadPar(par)
        self.groundRangePS = float(par.range_pixel_spacing)/(math.sin(math.radians(float(par.incidence_angle))))
        # compute initial multilooking factors
        if targetres == "automatic":
            if self.groundRangePS > float(par.azimuth_pixel_spacing):
                ratio = self.groundRangePS/float(par.azimuth_pixel_spacing)
                self.rlks = 1
                self.azlks = int(round(ratio))
            else:
                ratio = float(par.azimuth_pixel_spacing)/self.groundRangePS
                self.rlks = int(round(ratio))
                self.azlks = 1
        else:
            self.rlks = int(round(float(targetres)/self.groundRangePS))
            self.azlks = int(round(float(targetres)/float(par.azimuth_pixel_spacing)))


# create index objects containing paths to all products of a particular scene
# a list of entries can be queried by calling Tuple.__dict__.keys(); Tuple.index contains only those entries that represent individual images or image groups
class Tuple(object):
    def __init__(self, scene):
        self.index = []
        self.main = scene
        self.basename = self.main.strip("/").split("/")[-1]
        for x in [y for y in finder(scene, "*") if ".par" not in y and ".hdr" not in y]:
            base = os.path.basename(x)
            if re.search("[0-9]{8}T[0-9]{6}", base):
                tag = base[re.search("[0-9]{8}T[0-9]{6}", base).end()+1:]
                setattr(self, tag, x)
                self.index.append(tag)
        # append interferometric products
        isp_full = [y for y in finder(os.path.join(os.path.split(scene)[0], "ISP"), "*") if re.search("[0-9]{8}T[0-9]{6}", y) and not re.search("(?:bmp|hdr|par|kml)$", y)]
        isp_sub = [z for z in isp_full if re.findall("[0-9]{8}T[0-9]{6}", os.path.basename(z))[0] in self.basename]
        isp_tags = list(set([x[re.search(re.findall("[0-9]{8}T[0-9]{6}_[HV]{2}_", os.path.basename(x))[1], x).end():] for x in isp_sub]))
        for tag in isp_tags:
            setattr(self, tag, [x for x in isp_sub if re.search(tag+"$", x)])
            self.index.append(tag)
        self.index.sort()


# union of two lists
def union(a, b):
    return list(set(a) & set(b))


# convert a gamma parameter file corner coordinate from EQA to UTM
class UTM(object):
    def __init__(self, parfile):
        par = ReadPar(parfile)
        inlist = ["WGS84", "1", "EQA", par.corner_lon, par.corner_lat, "", "WGS84", "1", "UTM", ""]
        proc = sp.Popen(["coord_trans"], stdin=sp.PIPE, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True, shell=False).communicate("".join([x + "\n" for x in inlist]))
        proc = [x for x in filter(None, proc[0].split("\n")) if ":" in x]
        self.index = []
        for item in proc:
            entry = item.split(": ")
            entry = [entry[0].replace(" ", "_"), entry[1].split()]
            if len(entry[1]) > 1:
                setattr(self, entry[0], entry[1])
            else:
                setattr(self, entry[0], entry[1][0])
            self.index.append(entry[0])
            if "UTM" in entry[0]:
                self.zone, self.northing, self.easting = entry[1]
                self.index = list(set(self.index+["zone", "northing", "easting"]))


# write parameter textfile
def writer(filename, arguments, strfill=True):
    with open(filename, 'w') as out:
        for i in range(0, len(arguments)):
            if strfill:
                out.write(arguments[i][0].replace(" ", "_") + "\t" + arguments[i][1] + "\n")
            else:
                out.write(arguments[i][0] + "\t" + arguments[i][1] + "\n")
