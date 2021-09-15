from auxilliary.read_env import ReadEnv
import xml.etree.cElementTree as ET
import os
import re
from auxilliary.xml_creator import XMLCreaterGAMMA
import sys
# Author: Stefan Werner
# Implementation create_args_par_S1_GRD Felix Behrendt

class GammaArgs:
    """
    This is the Class witch contains all Methods which creates and returns
    the needed processing Arguments for the gamma processing for the API Modules.
    eg. gamma/gamma_modules/par_S1_SLC.py
    """

    def __init__(self):
        self.args = list()

    def create_args_par_S1_SLC(self):
        """
        This is the Function to Create all needed Arguments in the correct Order for the par_S1_SLC Module.
        Corresponding Window: QSubWindow_S1_TOPS.py, from here comes the Input over the API file par_S1_SLC.py
        This Function works like this:
            - WorkENV.xml, GammaCommands.xml are read and the Values are Extraxted (WorkEnv, idir, gammma_module_name)
            - The Import Directory contains: extracted *.zip Files in the *.SAFE Format
            - For every Folder (*.SAFE) a loop is executed:
                - The loop is searching in every *.SAFE Folder for the necessary Files and creates the corresponding Arguments for Gamma
                    - Input:
                        - GeoTIFFS
                        - annotation_XML
                        - calibration_XML
                        - noise_XML
                    - Output:
                        - Names for SLC_par
                        - Names for SLC
                        - Names for TOPS_par
                - The Loop Returns a List(1) of Lists(2),
                    - where the List(1)
                        representes the *.SAFE Folder
                    - and the corresponding List(2)
                        contains a List of Orderd Gamma Aruments (from the Folder Structure of the *.SAFE Folder)
            - For the Return Argument a loop is exucted:
                - This loop adjusts the Output to Linux Format
                - I could realy test where the output goes, i think in the home dir
            - To Clean up the Output another Loop is executed:
                - This loop creates a Folder and moves every corresponding processed Gamma Output to the Correct folder
                ------- Collecting all *SAFE Folders -------
                ['S1A_IW_SLC__1SDV_20170731T163002_20170731T163029_017717_01DAC5_4796.SAFE', 'S1A_IW_SLC__1SDV_20170812T163002_20170812T163029_017892_01E015_2E07.SAFE']
                ------- Collecting all GeoTIFFS from Folders -------
                ['s1a-iw1-slc-vh-20170731t163004-20170731t163029-017717-01dac5-001.tiff', 's1a-iw1-slc-vv-20170731t163004-20170731t163029-017717-01dac5-004.tiff', ...]
                ['s1a-iw1-slc-vh-20170812t163004-20170812t163029-017892-01e015-001.tiff', 's1a-iw1-slc-vv-20170812t163004-20170812t163029-017892-01e015-004.tiff', ...]
                ------- Collecting all annotation_XML from Folders -------
                ['s1a-iw1-slc-vh-20170731t163004-20170731t163029-017717-01dac5-001.xml', 's1a-iw1-slc-vv-20170731t163004-20170731t163029-017717-01dac5-004.xml', ...]
                ['s1a-iw1-slc-vh-20170812t163004-20170812t163029-017892-01e015-001.xml', 's1a-iw1-slc-vv-20170812t163004-20170812t163029-017892-01e015-004.xml', ...]
                ------- Collecting all calibration_XML from Folders -------
                ['calibration-s1a-iw1-slc-vh-20170731t163004-20170731t163029-017717-01dac5-001.xml', 'calibration-s1a-iw1-slc-vv-20170731t163004-20170731t163029-017717-01dac5-004.xml', ...]
                ['calibration-s1a-iw1-slc-vh-20170812t163004-20170812t163029-017892-01e015-001.xml', 'calibration-s1a-iw1-slc-vv-20170812t163004-20170812t163029-017892-01e015-004.xml', ...]
                ------- Collecting all noise_XML from Folders -------
                ['noise-s1a-iw1-slc-vh-20170731t163004-20170731t163029-017717-01dac5-001.xml', 'noise-s1a-iw1-slc-vv-20170731t163004-20170731t163029-017717-01dac5-004.xml', ...]
                ['noise-s1a-iw1-slc-vh-20170812t163004-20170812t163029-017892-01e015-001.xml', 'noise-s1a-iw1-slc-vv-20170812t163004-20170812t163029-017892-01e015-004.xml', ...]
                ------- Creating Basenames for Output Files -------
                S1A_IW_20170731T163002_A
                S1A_IW_20170812T163002_A
                ------- Creating Names for SLC_par Outputfiles -------
                ['S1A_IW_20170731T163002_A_iw1_vh.slc.par', 'S1A_IW_20170731T163002_A_iw1_vv.slc.par', ...]
                ['S1A_IW_20170812T163002_A_iw1_vh.slc.par', 'S1A_IW_20170812T163002_A_iw1_vv.slc.par', ...]
                ------- Creating Names for SLC Outputfiles -------
                ['S1A_IW_20170731T163002_A_iw1_vh.slc', 'S1A_IW_20170731T163002_A_iw1_vv.slc', ...]
                ['S1A_IW_20170812T163002_A_iw1_vh.slc', 'S1A_IW_20170812T163002_A_iw1_vv.slc', ...]
                ------- Creating Names for TOPS_PAR Outputfiles -------
                ['S1A_IW_20170731T163002_A_iw1_vh.slc.par', 'S1A_IW_20170731T163002_A_iw1_vv.slc.par', ...]
                ['S1A_IW_20170812T163002_A_iw1_vh.slc.par', 'S1A_IW_20170812T163002_A_iw1_vv.slc.par', ...]
                ------- RETURD ARGUMENTS --------
                par_S1_SLC s1a-iw1-slc-vh-20170731t163004-20170731t163029-017717-01dac5-001.tiff s1a-iw1-slc-vh-20170731t163004-20170731t163029-017717-01dac5-001.xml calibration-s1a-iw1-slc-vh-20170731t163004-20170731t163029-017717-01dac5-001.xml noise-s1a-iw1-slc-vh-20170731t163004-20170731t163029-017717-01dac5-001.xml S1A_IW_20170731T163002_A_iw1_vh.slc.par S1A_IW_20170731T163002_A_iw1_vh.slc S1A_IW_20170731T163002_A_iw1_vh.tops_par 0 60.000
                par_S1_SLC s1a-iw1-slc-vv-20170731t163004-20170731t163029-017717-01dac5-004.tiff s1a-iw1-slc-vv-20170731t163004-20170731t163029-017717-01dac5-004.xml calibration-s1a-iw1-slc-vv-20170731t163004-20170731t163029-017717-01dac5-004.xml noise-s1a-iw1-slc-vv-20170731t163004-20170731t163029-017717-01dac5-004.xml S1A_IW_20170731T163002_A_iw1_vv.slc.par S1A_IW_20170731T163002_A_iw1_vv.slc S1A_IW_20170731T163002_A_iw1_vv.tops_par 0 60.000
                ------- Adjust to Linux ---------
                par_S1_SLC $(find . -iname s1a-iw1-slc-vh-20170731t163004-20170731t163029-017717-01dac5-001.tiff) $(find . -iname s1a-iw1-slc-vh-20170731t163004-20170731t163029-017717-01dac5-001.xml)
                par_S1_SLC $(find . -iname s1a-iw1-slc-vv-20170731t163004-20170731t163029-017717-01dac5-004.tiff) $(find . -iname s1a-iw1-slc-vv-20170731t163004-20170731t163029-017717-01dac5-004.xml)
                ------- Move the Files to Folder ------
                mkdir S1A_IW_20170731T163002_A && mv S1A_IW_20170731T163002_A_iw1_vh.slc.par "$_" && mv S1A_IW_20170731T163002_A_iw1_vh.slc "$_" && mv S1A_IW_20170731T163002_A_iw1_vh.tops_par "$_" ...
                mkdir S1A_IW_20170812T163002_A && mv S1A_IW_20170812T163002_A_iw1_vh.slc.par "$_" && mv S1A_IW_20170812T163002_A_iw1_vh.slc "$_" && mv S1A_IW_20170812T163002_A_iw1_vh.tops_par "$_" ...
        :return: tuble of Arguments
        """
        # TODO HANDLE "missing" args or different Default Values
        # Create List for all the Arguments
        args = self.args

        # Make Instance of WorkENV.xml and read it
        my_dir = ReadEnv()
        WorkEnv = my_dir.read_env()

        # Make Instance of XMLCreaterGAMMA and Read the par_S1_SLC Command
        gamma = XMLCreaterGAMMA()
        gamma_com = gamma.read_XMLGAMMA("par_S1_SLC")

        print("------- Creating necessary Variables --------")
        # Create Import Dir
        idir = WorkEnv[1]

        # Create Output Dir -> I Think not necessary in this Case ... Gamma Processing
        odir = WorkEnv[3]

        # Root the WorkENV.xml
        root = ET.parse(WorkEnv[4]).getroot()
        print(root)

        # Define Folder Ending (for Sentinel *.SAFE)
        extension = ".SAFE"

        # Create List for all *.SAFE Folders (TopList of the List in List)
        folders = list()

        ### Gamma Commands
        # GAMMA Input
        GeoTIFF = list()  # includes list of tiffs
        annotation_XML = list()
        calibration_XML = list()
        noise_XML = list()

        # Gamma Output
        outname_base = list()
        outname_SLC_par = list()
        outname_SLC = list()
        outname_SLC_tops_par = list()
        dytpe = "0"  # 0 is default(FCOMPLEX), 1 (SCOMPLEX)
        sc_dB = "60.000"  # Scale Factro for FCOMPLEX -> SCOMPLEX, default HH,VV (dB): 60.000 , VH,HV: 70.000

        print("------- Reading S1_TOPS Data *.SAFE FORMAT --------")

        print("------- Collecting all *SAFE Folders -------")
        # GeoTIFF, annotation_XML, calibration_XML, noise_XML, SLC_par, SLC, TOPS_par, dtype, sc_dB
        for i in os.listdir(idir):  # loop through items in dir
            if i.endswith(extension):  # check for ".zip" extension
                folders.append(i)
        print(folders)

        print("------- Collecting all GeoTIFFS from Folders -------")
        for i in folders:
            subfoldtmp = list()
            for j in os.listdir(os.path.join(idir, i, "measurement")):
                subfoldtmp.append(j)
            GeoTIFF.append(subfoldtmp)
        for i in GeoTIFF:
            print(i)

        print("------- Collecting all annotation_XML from Folders -------")
        for i in folders:
            subfoldtmp = list()
            for j in os.listdir(os.path.join(idir, i, "annotation")):
                if j.endswith(".xml"):
                    subfoldtmp.append(j)
            annotation_XML.append(subfoldtmp)
        for i in annotation_XML:
            print(i)

        print("------- Collecting all calibration_XML from Folders -------")
        for i in folders:
            subfoldtmp = list()
            for j in os.listdir(os.path.join(idir, i, "annotation", "calibration")):
                if j.startswith("calibration"):
                    subfoldtmp.append(j)
                    calibration_XML.append(subfoldtmp)
            calibration_XML.append(subfoldtmp)
        for i in calibration_XML:
            print(i)

        print("------- Collecting all noise_XML from Folders -------")
        for i in folders:
            subfoldtmp = list()
            for j in os.listdir(os.path.join(idir, i, "annotation", "calibration")):
                if j.startswith("noise"):
                    #subfoldtmp.append(os.path.join(i, "annotation", "calibration", j))
                    #subfoldtmp.append(j) #WARNING: noise level values file: NESZ value(s) above -20 dB found (inf dB),WARNING: noise level values will not be used
                    subfoldtmp.append("-")
            noise_XML.append(subfoldtmp)
        for i in noise_XML:
            print(i)

        print("------- Creating Basenames for Output Files -------")
        # Pattern for Naming Convention -> siehe John?!
        # S1_main.py gammaGUI
        pattern = r"^(?P<sat>S1[AB])_(?P<beam>S1|S2|S3|S4|S5|S6|IW|EW|WV|EN|N1|N2|N3|N4|N5|N6|IM)_(?P<prod>SLC|GRD|OCN)(?:F|H|M|_)_(?:1|2)(?P<class>S|A)(?P<pols>SH|SV|DH|DV|HH|HV|VV|VH)_(?P<start>[0-9]{8}T[0-9]{6})_(?P<stop>[0-9]{8}T[0-9]{6})_(?:[0-9]{6})_(?:[0-9A-F]{6})_(?:[0-9A-F]{4})\.SAFE$"

        for i in range(len(folders)):
            match = re.match(pattern, folders[i])
            orbit = "D" if float(re.findall("[0-9]{6}", match.group("start"))[1]) < 120000 else "A"
            # self.outname_base_tmp = "_".join([os.path.join(idir, match.group("sat")), match.group("beam"), match.group("start").replace("T", "_"),orbit])
            outname_base_tmp = "_".join(
                [match.group("sat"), match.group("beam"), match.group("start"), orbit])
            # print(self.outname_base_tmp)
            outname_base.append(outname_base_tmp)
        for i in outname_base:
            print(i)
        # print(self.outname_base)

        print("------- Creating Names for SLC_par Outputfiles -------")
        # Pattern for _iw*_vv.slc.par
        pattern = r"^(?P<sat>s1[ab]\-(?P<beam>iw1|iw2|iw3)\-(?P<prod>slc)\-(?P<pols>vv|vh)*)"
        # print(pattern)
        for i in range(len(GeoTIFF)):
            suboutname_tmp = list()
            for j in range(len(GeoTIFF[i])):
                match = re.match(pattern, GeoTIFF[i][j])
                # print(match)
                # self.outname_tmp = "_".join(
                #     [match.group("beam"),match.group("pols"),".SLC.par"]).replace("D","")
                # print(self.outname_tmp)
                suboutname_tmp.append(("_".join(
                    [outname_base[i], match.group("beam"), match.group("pols"), ".slc.par"]).replace("D",
                                                                                                     "")).replace(
                    "_.slc", ".slc"))
            # print(self.suboutname_tmp)
            outname_SLC_par.append(suboutname_tmp)
        for i in outname_SLC_par:
            print(i)
        # print(self.outname_SLC_par)

        print("------- Creating Names for SLC Outputfiles -------")

        # Pattern for _iw1_vv.slc.par
        pattern = r"^(?P<sat>s1[ab]\-(?P<beam>iw1|iw2|iw3)\-(?P<prod>slc)\-(?P<pols>vv|vh)*)"
        # print(pattern)

        for i in range(len(GeoTIFF)):
            suboutname_tmp = list()
            for j in range(len(GeoTIFF[i])):
                match = re.match(pattern, GeoTIFF[i][j])
                # print(match)
                # self.outname_tmp = "_".join(
                #     [match.group("beam"),match.group("pols"),".SLC.par"]).replace("D","")
                # print(self.outname_tmp)
                suboutname_tmp.append(("_".join(
                    [outname_base[i], match.group("beam"), match.group("pols"), ".slc"]).replace("D", "")).replace(
                    "_.slc", ".slc"))
            # print(self.suboutname_tmp)
            outname_SLC.append(suboutname_tmp)
        for i in outname_SLC:
            print(i)
        # print(self.outname_SLC)

        print("------- Creating Names for TOPS_PAR Outputfiles -------")
        # Pattern for _iw1_vv.slc.par
        pattern = r"^(?P<sat>s1[ab]\-(?P<beam>iw1|iw2|iw3)\-(?P<prod>slc)\-(?P<pols>vv|vh)*)"
        # print(pattern)

        for i in range(len(GeoTIFF)):
            suboutname_tmp = list()
            for j in range(len(GeoTIFF[i])):
                match = re.match(pattern, GeoTIFF[i][j])
                # print(match)
                # self.outname_tmp = "_".join(
                #     [match.group("beam"),match.group("pols"),".SLC.par"]).replace("D","")
                # print(self.outname_tmp)
                suboutname_tmp.append(("_".join(
                    [outname_base[i], match.group("beam"), match.group("pols"), ".tops_par"]).replace("D",
                                                                                                           "")).replace(
                    "_.tops_par", ".tops_par"))
            # print(self.suboutname_tmp)
            outname_SLC_tops_par.append(suboutname_tmp)

        for i in outname_SLC_par:
            print(i)

        print("------- Transforming to Linux Syntax -------")
        for i in range(len(GeoTIFF)):
            for j in range(len(GeoTIFF[i])):
                print((" ".join([gamma_com, "".join(["$(find . -iname ", GeoTIFF[i][j], ")"]),
                                 "".join(["$(find . -iname ", annotation_XML[i][j], ")"]),
                                 "".join(["$(find . -iname ", calibration_XML[i][j], ")"]),
                                # "".join(["$(find . -iname ", noise_XML[i][j], ")"]),
                                 noise_XML[i][j],
                                 outname_SLC_par[i][j], outname_SLC[i][j],
                                 outname_SLC_tops_par[i][j], dytpe, sc_dB])))
                # tmp_args = (" ".join([gamma_com, GeoTIFF[i][j], annotation_XML[i][j],
                #                 calibration_XML[i][j], noise_XML[i][j],
                #                 outname_SLC_par[i][j], outname_SLC[i][j],
                #                 outname_SLC_tops_par[i][j], dytpe, sc_dB])) # Potentielly add str(sys.executable), str(sys.argv[0]), at the beginning
                tmp_args = (" ".join([gamma_com, "".join(["$(find . -iname ", GeoTIFF[i][j], ")"]),
                                 "".join(["$(find . -iname ", annotation_XML[i][j], ")"]),
                                 "".join(["$(find . -iname ", calibration_XML[i][j], ")"]),
                                 #"".join(["$(find . -iname ", noise_XML[i][j], ")"]),
                                 noise_XML[i][j],
                                outname_SLC_par[i][j], outname_SLC[i][j],
                                outname_SLC_tops_par[i][j], dytpe, sc_dB]))

                args.append(tmp_args)
                #print("XML_S1_TOPS" +" "+ self.GeoTIFF[i][j] +" "+ self.annotation_XML[i][j] )
                #run(["XML_S1_TOPS", self.GeoTIFF[i][j]])


        # print("This are my ARGS to PASS TO S1_TOPS.py -> Run S1 TOPS")
        # print(args)
        print("------- Creating Arguments to copy produced SLC Files to its own folder")

        #mkdir S1A_IW_20170731T163002_A && mv S1A_IW_20170731T163002_A_iw1_vh.slc.par "$_" && mv S1A_IW_20170731T163002_A_iw1_vh.slc"$_" && mv S1A_IW_20170731T163002_A_iw1_vh.tops_par"$_"
        # mkdir basename && mv outname_SLC_par "$_" && outname_SLC "$_" && outname_SLC_par "$_" (für alle iw + vv,vh)

        # Create list for Copy Args
        copy_args = list()
        for i in range(len(outname_base)):
            print((" ".join(["mkdir", outname_base[i],
                             " ".join(["&& mv", outname_SLC_par[i][0],'"$_"'])," ".join(["&& mv", outname_SLC[i][0], '"$_"']), " ".join(["&& mv", outname_SLC_tops_par[i][0], '"$_"']),
                             " ".join(["&& mv", outname_SLC_par[i][1], '"$_"'])," ".join(["&& mv", outname_SLC[i][1], '"$_"'])," ".join(["&& mv", outname_SLC_tops_par[i][1], '"$_"']),
                             " ".join(["&& mv", outname_SLC_par[i][2], '"$_"'])," ".join(["&& mv", outname_SLC[i][2], '"$_"'])," ".join(["&& mv", outname_SLC_tops_par[i][2], '"$_"']),
                             " ".join(["&& mv", outname_SLC_par[i][3], '"$_"'])," ".join(["&& mv", outname_SLC[i][3], '"$_"'])," ".join(["&& mv", outname_SLC_tops_par[i][3], '"$_"']),
                             " ".join(["&& mv", outname_SLC_par[i][4], '"$_"'])," ".join(["&& mv", outname_SLC[i][4], '"$_"'])," ".join(["&& mv", outname_SLC_tops_par[i][4], '"$_"']),
                             " ".join(["&& mv", outname_SLC_par[i][5], '"$_"'])," ".join(["&& mv", outname_SLC[i][5], '"$_"'])," ".join(["&& mv", outname_SLC_tops_par[i][5], '"$_"'])])))
            copy_args_tmp = (" ".join(["mkdir", outname_base[i], # TODO Find out behaviour on Server possibly Change Linux Syntax
                             " ".join(["&& mv", outname_SLC_par[i][0],'"$_"'])," ".join(["&& mv", outname_SLC[i][0], '"$_"']), " ".join(["&& mv", outname_SLC_tops_par[i][0], '"$_"']),
                             " ".join(["&& mv", outname_SLC_par[i][1], '"$_"'])," ".join(["&& mv", outname_SLC[i][1], '"$_"'])," ".join(["&& mv", outname_SLC_tops_par[i][1], '"$_"']),
                             " ".join(["&& mv", outname_SLC_par[i][2], '"$_"'])," ".join(["&& mv", outname_SLC[i][2], '"$_"'])," ".join(["&& mv", outname_SLC_tops_par[i][2], '"$_"']),
                             " ".join(["&& mv", outname_SLC_par[i][3], '"$_"'])," ".join(["&& mv", outname_SLC[i][3], '"$_"'])," ".join(["&& mv", outname_SLC_tops_par[i][3], '"$_"']),
                             " ".join(["&& mv", outname_SLC_par[i][4], '"$_"'])," ".join(["&& mv", outname_SLC[i][4], '"$_"'])," ".join(["&& mv", outname_SLC_tops_par[i][4], '"$_"']),
                             " ".join(["&& mv", outname_SLC_par[i][5], '"$_"'])," ".join(["&& mv", outname_SLC[i][5], '"$_"'])," ".join(["&& mv", outname_SLC_tops_par[i][5], '"$_"'])]))
            copy_args.append(copy_args_tmp)


        print("Creating Tuple and Returning it to the API File: par_S1_SLC.py")
        my_tuple = tuple((args, copy_args))

        return my_tuple

        #TODO
        # create_args_{xy} for further Processing Sequence
        # -> in gamma/gamma_modules/S1_TOPS.py just implement the right order for S1_TOPS data

    def create_args_par_S1_GRD(self):
        """
        Original Code by Stefan, Implementation by Felix
        No tests executed
        :return:
        """
        print("Start Import S1 GRD")
        args = self.args

        # Make Instance of WorkENV.xml and read it
        my_dir = ReadEnv()
        WorkEnv = my_dir.read_env()

        # Make Instance of XMLCreaterGAMMA and Read the par_S1_SLC Command
        gamma = XMLCreaterGAMMA()
        gamma_com = gamma.read_XMLGAMMA("par_S1_GRD")
        # print(gamma_com)

        # print("------- Print Work ENV ------")
        # print(WorkEnv)
        print("------- Creating necessary Variables --------")
        # Create Import Dir
        idir = WorkEnv[1]
        # idir = "C:/Users/kbehr/Desktop/Gamma/Test"
        print(idir)

        # Create Output Dir -> I Think not necessary in this Case ... Gamma Processing
        odir = WorkEnv[3]
        # print(odir)

        # Root the WorkENV.xml
        root = ET.parse(WorkEnv[4]).getroot()
        print(root)

        # Define Folder Ending (for Sentinel *.SAFE)
        extension = ".SAFE"

        # Create List for all *.SAFE Folders (TopList of the List in List)
        folders = list()

        # Define Variables Gamma needs -> everything a list (Lists in TopLists)
        # List for basenames
        outname_base = list()

        # GAMMA Input
        GeoTIFF = list()  # includes list of tiffs
        annotation_XML = list()
        calibration_XML = list()
        noise_XML = list()

        # Gamma Output
        outname_MLI_par = list()
        outname_MLI = list()

        # Todo : Add optional parameter for extrapolation

        # optional parameter
        outname_GRD_par = "-"
        outname_GRD = "-"
        eflg = "0"  # GR-SR grid extrapolation flag: 0 --> NO Extrapolation (Advised),
        rps = ""  # Slant Range pixel spacing (m) -->
        noise_pwr = ""  # noise intensity for each MLI sample in slant range using data from noise_XML

        print("Import dir: " + idir)
        print("Export dir: " + odir)
        print("Root:")
        print(root)

        print("------- Reading S1_GRD Data *.SAFE FORMAT --------")

        print("------- Collecting all *SAFE Folders -------")
        # GeoTIFF, annotation_XML, calibration_XML, noise_XML,
        for i in os.listdir(idir):  # loop through items in dir
            if i.endswith(extension):  # check for ".zip" extension
                folders.append(i)
        print(folders)

        print("------- Collecting all GeoTIFFS from Folders -------")
        for i in folders:
            subfoldtmp = list()
            for j in os.listdir(os.path.join(idir, i, "measurement")):
                subfoldtmp.append(j)
            GeoTIFF.append(subfoldtmp)
        for i in GeoTIFF:
            print(i)

        print("------- Collecting all annotation_XML from Folders -------")
        for i in folders:
            subfoldtmp = list()
            for j in os.listdir(os.path.join(idir, i, "annotation")):
                if j.endswith(".xml"):
                    subfoldtmp.append(j)
            annotation_XML.append(subfoldtmp)
        for i in annotation_XML:
            print(i)

        print("------- Collecting all calibration_XML from Folders -------")
        for i in folders:
            subfoldtmp = list()
            for j in os.listdir(os.path.join(idir, i, "annotation", "calibration")):
                if j.startswith("calibration"):
                    subfoldtmp.append(j)
                    calibration_XML.append(subfoldtmp)
            calibration_XML.append(subfoldtmp)
        for i in calibration_XML:
            print(i)

        print("------- Collecting all noise_XML from Folders -------")
        # TODO Optional Parameter to add thermal noise to the data
        for i in folders:
            subfoldtmp = list()
            for j in os.listdir(os.path.join(idir, i, "annotation", "calibration")):
                if j.startswith("noise"):
                    subfoldtmp.append("-")  # thermal noise is already deleted --> to add back  activate line above
            noise_XML.append(subfoldtmp)
        for i in noise_XML:
            print(i)

        print("------- Creating Basenames for Output Files -------")
        #
        pattern = r"^(?P<sat>S1[AB])_(?P<beam>S1|S2|S3|S4|S5|S6|IW|EW|WV|EN|N1|N2|N3|N4|N5|N6|IM)_(?P<prod>SLC|GRD|OCN)(?:F|H|M|_)_(?:1|2)(?P<class>S|A)(?P<pols>SH|SV|DH|DV|HH|HV|VV|VH)_(?P<start>[0-9]{8}T[0-9]{6})_(?P<stop>[0-9]{8}T[0-9]{6})_(?:[0-9]{6})_(?:[0-9A-F]{6})_(?:[0-9A-F]{4})\.SAFE$"

        for i in range(len(folders)):
            match = re.match(pattern, folders[i])
            orbit = "D" if float(re.findall("[0-9]{6}", match.group("start"))[1]) < 120000 else "A"
            # self.outname_base_tmp = "_".join([os.path.join(idir, match.group("sat")), match.group("beam"), match.group("start").replace("T", "_"),orbit])
            outname_base_tmp = "_".join(
                [match.group("sat"), match.group("beam"), match.group("start"), orbit])
            # print(self.outname_base_tmp)
            outname_base.append(outname_base_tmp)
        for i in outname_base:
            print(i)

        print("------- Creating Names for MLI Outputfiles -------")

        # Pattern for _iw1_vv.slc.par
        pattern = r"^(?P<sat>s1[ab]\-(?P<beam>iw)\-(?P<prod>grd)\-(?P<pols>vv|vh)*)"
        # print(pattern)

        for i in range(len(GeoTIFF)):
            suboutname_tmp1 = list()
            suboutname_tmp2 = list()
            for j in range(len(GeoTIFF[i])):
                match = re.match(pattern, GeoTIFF[i][j])
                suboutname_tmp1.append(("_".join(
                    [outname_base[i], match.group("beam"), match.group("pols"), ".mli"]).replace("_D", "")).replace(
                    "_.mli", ".ml.mli"))
                suboutname_tmp2.append(("_".join(
                    [outname_base[i], match.group("beam"), match.group("pols"), ".mli"]).replace("_D", "")).replace(
                    "_.mli", ".ml.mli.par"))
            outname_MLI.append(suboutname_tmp1)
            outname_MLI_par.append(suboutname_tmp2)
        for i in outname_MLI:
            print(i)

        print("------- Creating Names for MLI_PAR Outputfiles -------")
        for i in outname_MLI_par:
            print(i)

        print("------- Creates argumente for PAR_S1_GRD -------")
        for i in range(len(GeoTIFF)):
            for j in range(len(GeoTIFF[i])):
                print((" ".join([gamma_com, "".join(["$(find . -iname ", GeoTIFF[i][j], ")"]),
                                 "".join(["$(find . -iname ", annotation_XML[i][j], ")"]),
                                 "".join(["$(find . -iname ", calibration_XML[i][j], ")"]),
                                # "".join(["$(find . -iname ", noise_XML[i][j], ")"]),
                                 noise_XML[i][j],
                                 outname_MLI_par[i][j], outname_MLI[i][j],
                                 outname_GRD_par, outname_GRD, eflg, rps, noise_pwr])))

                tmp_args = (" ".join([gamma_com, "".join(["$(find . -iname ", GeoTIFF[i][j], ")"]),
                                 "".join(["$(find . -iname ", annotation_XML[i][j], ")"]),
                                 "".join(["$(find . -iname ", calibration_XML[i][j], ")"]),
                                 #"".join(["$(find . -iname ", noise_XML[i][j], ")"]),
                                 noise_XML[i][j],
                                outname_MLI_par[i][j], outname_MLI[i][j],
                                outname_GRD_par, outname_GRD, eflg, rps, noise_pwr]))

                args.append(tmp_args)


        # Create list for Copy Args
        copy_args = list()
        print(copy_args)

        for i in range(len(outname_base)):
            print("Hallo")
            print((" ".join(["mkdir", outname_base[i],
                             " ".join(["&& mv", outname_MLI_par[i][0],'"$_"'])," ".join(["&& mv", outname_MLI[i][0], '"$_"']),
                             " ".join(["&& mv", outname_MLI_par[i][1], '"$_"'])," ".join(["&& mv", outname_MLI[i][1], '"$_"'])])))

            copy_args_tmp = (" ".join(["mkdir", outname_base[i], # TODO Find out behaviour on Server possibly Change Linux Syntax
                             " ".join(["&& mv", outname_MLI_par[i][0],'"$_"'])," ".join(["&& mv", outname_MLI[i][0], '"$_"']),
                             " ".join(["&& mv", outname_MLI_par[i][1], '"$_"'])," ".join(["&& mv", outname_MLI[i][1], '"$_"'])]))
            copy_args.append(copy_args_tmp)

        print("Print jetzt die Argzmente zum in der Liste Kopieren der SLO Daten")
        for i in copy_args:
            print(i)





        my_tuple = tuple((args, copy_args))
        print(my_tuple)
        print("------- Returning Collected Arguments to S1_TOPS.py to run par_S1_SLC Gamma Module -------")

        # return args,copy_args
        return my_tuple

if __name__ == '__main__':
    t = GammaArgs()
    print(t)
    t.create_args_par_S1_SLC()
    t.create_args_par_S1_GRD()