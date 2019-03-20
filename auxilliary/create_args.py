from auxilliary.read_env import ReadEnv
import xml.etree.cElementTree as ET
import os
import re
from auxilliary.xml_creator import XMLCreaterGAMMA
import sys

class Args:
    """
    This is the Class for all Arguments which are passed to the GammaSoftware. The Script where the Commands are passed
    is e.g. gamma/gamma_modules/S1_TOPS.py
    Aim of this Class is to contain all necessary Methods to create the specific Arguments (in the correct Order)
    which should be passed to the corresponding GammaSoftware Module e.g. create_args_S1_TOPS()
    The Output goes to gamma/gamma_modules/S1_TOPS.py where the Arguments are given to the shell
    """

    def __init__(self):
        self.args = list()

    def create_args_par_S1_SLC(self):
        """
        This is the Function to Create all needed Arguments in the correct Order for the par_S1_SLC Module.
        Corresponding Window: gammaGUIv2/gui_windows/QSubWindow_S1_TOPS.py where the Input comes from
        Therefore:
            - the WorkEnv.xml,GammaCommands.xml is read and the WorkEnv and Import Directory are extracted
            - The Import Directory contains: the Extracted *zip Files in the *.SAFE Format
            - For every Folder (*.SAFE) in this ImportDIR a loop is executed:
                - The loop searches in the *.SAFE Folder for all necessary Files and Creates the corresponding Outputfilenames:
                    - Input:
                        - GeoTIFFS
                        - annotation_XML
                        - calibration_XML
                        - noise_XML
                    - Output:
                        - Names for SLC_par
                        - Names for SLC
                        - Names for TOPS_par
                - The Loop Returns a List of Lists, where a List corresponds to a specific *SAFE Folder
                    and contains a List of needed Arguments.

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

        :return:
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
        #print(gamma_com)

        # print("------- Print Work ENV ------")
        # print(WorkEnv)
        print("------- Creating necessary Variables --------")
        # Create Import Dir
        idir = WorkEnv[1]
        #print(idir)

        # Create Output Dir -> I Think not necessary in this Case ... Gamma Processing
        odir = WorkEnv[3]
        #print(odir)

        # Root the WorkENV.xml
        root = ET.parse(WorkEnv[4]).getroot()
        print(root)

        # Define Folder Ending (for Sentinel *.SAFE)
        extension = ".SAFE"

        # Create List for all *.SAFE Folders (TopList of the List in List)
        folders = list()

        # Define Variables Gamma needs -> everything a list (Lists in TopLists)

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

        # print("Import dir: " + idir)
        # print("Export dir: " + odir)
        # print("Root:")
        # print(root)

        print("------- Reading S1_TOPS Data *.SAFE FORMAT --------")

        print("------- Collecting all *SAFE Folders -------")
        # GeoTIFF, annotation_XML, calibration_XML, noise_XML, SLC_par, SLC, TOPS_par, dtype,sc_dB
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
        for i in calibration_XML:
            print(i)

        print("------- Collecting all noise_XML from Folders -------")
        for i in folders:
            subfoldtmp = list()
            for j in os.listdir(os.path.join(idir, i, "annotation", "calibration")):
                if j.startswith("noise"):
                    subfoldtmp.append(j)
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

        # print(self.outname_SLC_tops_par)


        for i in range(len(GeoTIFF)):
            for j in range(len(GeoTIFF[i])):
                # print((" ".join([gamma_com, GeoTIFF[i][j], annotation_XML[i][j],
                #                 calibration_XML[i][j], noise_XML[i][j],
                #                 outname_SLC_par[i][j], outname_SLC[i][j],
                #                 outname_SLC_tops_par[i][j], dytpe, sc_dB])))
                tmp_args = (" ".join([gamma_com, GeoTIFF[i][j], annotation_XML[i][j],
                                calibration_XML[i][j], noise_XML[i][j],
                                outname_SLC_par[i][j], outname_SLC[i][j],
                                outname_SLC_tops_par[i][j], dytpe, sc_dB])) # Potentielly add str(sys.executable), str(sys.argv[0]), at the beginning

                args.append(tmp_args)
                #print("XML_S1_TOPS" +" "+ self.GeoTIFF[i][j] +" "+ self.annotation_XML[i][j] )
                #run(["XML_S1_TOPS", self.GeoTIFF[i][j]])


        # print("This are my ARGS to PASS TO S1_TOPS.py -> Run S1 TOPS")
        # print(args)

        print("------- Returning Collected Arguments to S1_TOPS.py to run par_S1_SLC Gamma Module -------")

        return args

        #TODO
        # create_args_{xy} for further Processing Sequence
        # -> in gamma/gamma_modules/S1_TOPS.py just implement the right order for S1_TOPS data

if __name__ == '__main__':
    t = Args()
    print(t)
    t.create_args_par_S1_SLC()