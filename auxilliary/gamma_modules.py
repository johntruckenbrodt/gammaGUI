# Searches for Files for Import to Gamma
# Inheriate readers from gammaGUI
# Adjust these ?!

import os
from auxilliary.read_env import ReadEnv
import xml.etree.cElementTree as ET
import re



class S1_TOPS():

    def __init__(self, idir, odir):
        self.idir
        self.odir

    def module_S1_TOPS(self, idir, odir):
        print("------- Reading S1_TOPS Data *.SAFE FORMAT --------")
        self.idir = idir
        self.odir = odir
        self.root = ET.parse(r"D:\gammaGUIv2\auxilliary\WorkEnv.xml").getroot()
        self.extension = ".SAFE"
        self.folders = list()
        # GAMMA Input
        self.GeoTIFF = list() # includes list of tiffs
        self.annotation_XML = list()
        self.calibration_XML = list()
        self.noise_XML = list()
        # Gamma Output
        self.outname_base = list()
        self.outname_SLC_par = list()
        self.outname_SLC = list()
        self.outname_SLC_tops_par = list()
        self.dytpe = "0" # 0 is default(FCOMPLEX), 1 (SCOMPLEX)
        self.sc_dB = "60.000" # Scale Factro for FCOMPLEX -> SCOMPLEX, default HH,VV (dB): 60.000 , VH,HV: 70.000


        print("Import dir: " + self.idir)
        print("Export dir: " + self.odir)
        print("Root:" )
        print(self.root)

        print("------- Collecting all *SAFE Folders -------")
        # GeoTIFF, annotation_XML, calibration_XML, noise_XML, SLC_par, SLC, TOPS_par, dtype,sc_dB
        for i in os.listdir(self.idir):  # loop through items in dir
            if i.endswith(self.extension):  # check for ".zip" extension
                self.folders.append(i)
        print(self.folders)

        print("------- Collecting all GeoTIFFS from Folders -------")
        for i in self.folders:
            self.subfoldtmp = list()
            for j in os.listdir(os.path.join(self.idir,i,"measurement")):
                self.subfoldtmp.append(j)
            self.GeoTIFF.append(self.subfoldtmp)
        for i in self.GeoTIFF:
            print(i)

        print("------- Collecting all annotation_XML from Folders -------")
        for i in self.folders:
            self.subfoldtmp = list()
            for j in os.listdir(os.path.join(self.idir,i,"annotation")):
                if j.endswith(".xml"):
                    self.subfoldtmp.append(j)
            self.annotation_XML.append(self.subfoldtmp)
        for i in self.annotation_XML:
            print(i)

        print("------- Collecting all calibration_XML from Folders -------")
        for i in self.folders:
            self.subfoldtmp = list()
            for j in os.listdir(os.path.join(self.idir, i, "annotation", "calibration")):
                if j.startswith("calibration"):
                    self.subfoldtmp.append(j)
            self.calibration_XML.append(self.subfoldtmp)
        for i in self.calibration_XML:
            print(i)

        print("------- Collecting all noise_XML from Folders -------")
        for i in self.folders:
            self.subfoldtmp = list()
            for j in os.listdir(os.path.join(self.idir,i,"annotation","calibration")):
                if j.startswith("noise"):
                    self.subfoldtmp.append(j)
            self.noise_XML.append(self.subfoldtmp)
        for i in self.noise_XML:
            print(i)

        print("------- Creating Basenames for Output Files -------")
        # Pattern for Naming Convention -> siehe John?!
        # S1_main.py gammaGUI
        pattern = r"^(?P<sat>S1[AB])_(?P<beam>S1|S2|S3|S4|S5|S6|IW|EW|WV|EN|N1|N2|N3|N4|N5|N6|IM)_(?P<prod>SLC|GRD|OCN)(?:F|H|M|_)_(?:1|2)(?P<class>S|A)(?P<pols>SH|SV|DH|DV|HH|HV|VV|VH)_(?P<start>[0-9]{8}T[0-9]{6})_(?P<stop>[0-9]{8}T[0-9]{6})_(?:[0-9]{6})_(?:[0-9A-F]{6})_(?:[0-9A-F]{4})\.SAFE$"

        for i in range(len(self.folders)):
            match = re.match(pattern,self.folders[i])
            orbit = "D" if float(re.findall("[0-9]{6}", match.group("start"))[1]) < 120000 else "A"
            #self.outname_base_tmp = "_".join([os.path.join(idir, match.group("sat")), match.group("beam"), match.group("start").replace("T", "_"),orbit])
            self.outname_base_tmp = "_".join(
                [match.group("sat"), match.group("beam"), match.group("start"),orbit])
            #print(self.outname_base_tmp)
            self.outname_base.append(self.outname_base_tmp)
        for i in self.outname_base:
            print(i)
        #print(self.outname_base)

        print("------- Creating Names for SLC_par Outputfiles -------")

        # Pattern for _iw1_vv.slc.par
        pattern = r"^(?P<sat>s1[ab]\-(?P<beam>iw1|iw2|iw3)\-(?P<prod>slc)\-(?P<pols>vv|vh)*)"
        #print(pattern)
        for i in range(len(self.GeoTIFF)):
            self.suboutname_tmp = list()
            for j in range(len(self.GeoTIFF[i])):
                match = re.match(pattern, self.GeoTIFF[i][j])
                # print(match)
                # self.outname_tmp = "_".join(
                #     [match.group("beam"),match.group("pols"),".SLC.par"]).replace("D","")
                # print(self.outname_tmp)
                self.suboutname_tmp.append(("_".join(
                    [self.outname_base[i],match.group("beam"),match.group("pols"),".slc.par"]).replace("D","")).replace("_.slc",".slc"))
            #print(self.suboutname_tmp)
            self.outname_SLC_par.append(self.suboutname_tmp)
        for i in self.outname_SLC_par:
            print(i)
        #print(self.outname_SLC_par)

        print("------- Creating Names for SLC Outputfiles -------")

        # Pattern for _iw1_vv.slc.par
        pattern = r"^(?P<sat>s1[ab]\-(?P<beam>iw1|iw2|iw3)\-(?P<prod>slc)\-(?P<pols>vv|vh)*)"
        #print(pattern)


        for i in range(len(self.GeoTIFF)):
            self.suboutname_tmp = list()
            for j in range(len(self.GeoTIFF[i])):
                match = re.match(pattern, self.GeoTIFF[i][j])
                # print(match)
                # self.outname_tmp = "_".join(
                #     [match.group("beam"),match.group("pols"),".SLC.par"]).replace("D","")
                # print(self.outname_tmp)
                self.suboutname_tmp.append(("_".join(
                    [self.outname_base[i], match.group("beam"), match.group("pols"), ".slc"]).replace("D", "")).replace("_.slc",".slc"))
            #print(self.suboutname_tmp)
            self.outname_SLC.append(self.suboutname_tmp)
        for i in self.outname_SLC:
            print(i)
        #print(self.outname_SLC)

        print("------- Creating Names for TOPS_PAR Outputfiles -------")
        # Pattern for _iw1_vv.slc.par
        pattern = r"^(?P<sat>s1[ab]\-(?P<beam>iw1|iw2|iw3)\-(?P<prod>slc)\-(?P<pols>vv|vh)*)"
        #print(pattern)


        for i in range(len(self.GeoTIFF)):
            self.suboutname_tmp = list()
            for j in range(len(self.GeoTIFF[i])):
                match = re.match(pattern, self.GeoTIFF[i][j])
                # print(match)
                # self.outname_tmp = "_".join(
                #     [match.group("beam"),match.group("pols"),".SLC.par"]).replace("D","")
                # print(self.outname_tmp)
                self.suboutname_tmp.append(("_".join(
                    [self.outname_base[i], match.group("beam"), match.group("pols"), ".tops_par"]).replace("D", "")).replace(
                    "_.tops_par", ".tops_par"))
            #print(self.suboutname_tmp)
            self.outname_SLC_tops_par.append(self.suboutname_tmp)

        for i in self.outname_SLC_par:
            print(i)

        #print(self.outname_SLC_tops_par)

        print("------- Start Printing Arguments for GAMMA -------")
        print("------- Start Importing to GAMMA ------")

        for i in range(len(self.GeoTIFF)):
            for j in range(len(self.GeoTIFF[i])):
                print((" ".join(["XML_S1_TOPS", self.GeoTIFF[i][j], self.annotation_XML[i][j],
                                self.calibration_XML[i][j], self.noise_XML[i][j],
                                self.outname_SLC_par[i][j], self.outname_SLC[i][j],
                                self.outname_SLC_tops_par[i][j], self.dytpe, self.sc_dB])))
                #print("XML_S1_TOPS" +" "+ self.GeoTIFF[i][j] +" "+ self.annotation_XML[i][j] )
                #run(["XML_S1_TOPS", self.GeoTIFF[i][j]])


        # for item in files_mli:
        #     run(["multi_look_MLI", item, item + ".par", item[:-3] + "mli2", item[:-3] + "mli2.par", rlks, azlks],
        #         logpath=path_log)
        print("------- ALL DATA IMPORTET ------")

        print("------- CREATE XML FILE FOR *.slc.par and *.tops.par ------")

        #TODO Implement XML Creater
        #TODO Rewrite Script to Object
        #TODO WRITE FUNCTION TO READ XML FILE AND READ ML FACKTOR AND SO ON








            #self.outname_base.append(self.outname_tmp)
        #print(self.outname_base)









        # match = re.match(pattern, self.folders[0])
        # print(match)
        # orbit = "D" if float(re.findall("[0-9]{6}", match.group("start"))[1]) < 120000 else "A"
        # print(orbit)
        # outname_base = "_".join([os.path.join(idir, match.group("sat")), match.group("beam"), match.group("start").replace("T", "_"),orbit])
        # print(outname_base)


        #GeoTIFF, annotation_XML, calibration_XML, noise_XML, SLC_par, SLC, TOPS_par, dtype,sc_dB
        #self.SLC_par = list()


if __name__ == '__main__':

    readed = S1_TOPS
    readed.module_S1_TOPS(readed,"D:\gammaGUIv2\data","D:\gammaGUIv2\data")

    print(readed)