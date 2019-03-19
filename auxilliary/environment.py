#!/usr/bin/env python
import os
import xml.etree.cElementTree as ET
from xml.dom import minidom

class Environment:

    """
    This is the Environment Class all Important Information are stored here
    #TODO MAKE IT TIDY
    #TODO find the POINT were are setting this  D:/gammaGUIv2,D:/gammaGUIv2/to_del, D:\gammaGUIv2\auxilliary\WorkEnv.xml make it to \\ -> better for UNIX / WINDOWS compatibility

    It's the Entry Point.

    Currently it setup the WorkENV.xml, if no xml Exists it is created via gammaGUIv2/gui_windows/QSubWindow_set_your_working_directory.py browsebutton
    If it exists nothing happens and the old WorkENV.xml is the old -> Should be no Problem should be dynamic and get New input via BrowseButtons and the set_idir Methods form this Class

    :var wdir path of current Working Directory
    :var idir path of current Import Directory
    :var odir path of current Output Directory
    :var tdir path of current Tmp Directory
    :var backgroundImage path to the BackgroundImage of the GUI
    :var gammaCommands  path to gammaCommands.xml

        ---> DO IT DIFFERENT <------------------------------------------------------------------------------------------
        ---> Define ENV HERE
        ---> TODO Work THIS OUT -> maybe it is implemented :D
        ---> Getter and posssinle. Setter are own python Scripts -> Stored in Auxiliary  --> to xml_creator
        ---> This contains different Classes for XML_Processing with methods -> e.g. create_XMLGAMMA, read_XMLGAMMA ;; create_XMLWorkENV, read_XMLWorkENV

    """
    # Define Class Variables
    # TODO
    #  IDEA: Check if WorkENV.xml exists and set this Values. If not set these.
    #       -> possibly my cause Problems

    wdir = os.getcwd()
    idir = "ImportDir"
    odir = "OutputDir"
    tdir = "TempDir"
    WorkEnv = os.path.join(wdir,"auxilliary","WorkEnv.xml")
    backgroundImage = os.path.join(os.getcwd(),"gammaGUIv2","gui_images","background.jpg")
    gammaCommands = os.path.join(wdir,"auxilliary","GammaCommands.xml")

    def set_wdir(self,wdir):
        """
        This the Function to set the initial WorkinDir. The Input comes from gammaGUIv2/gui_windows/QBrowseDialoge.py (Browse Folder Button)
        TODO see below
        It also creates the initial WorkENV.xml -> With the class Variables from Environment
        :param wdir:
        :return:
        """
        # TODO
        #   Change there the Function on OK Button
        #   Therefore:
        #       - Rewrite that the Output of QBrowseDialoge.py appears in the LineEdit Field in gammaGUIv2/gui_windows/QSubWindow_set_your_working_directory.py
        #       - Read this output and then Press Button und connenct this Function
        print(r"----- Welcome to the GammaGUIv2")
        print(r"----- Setting up your dynamic WorkENV")
        self.wdir = wdir
        print(r"Your Working Directory is: " + wdir)
        #print(self.wdir)
        print("----- Start Creating dynamic WorkENV")
        root = ET.Element("root")
        filename = self.WorkEnv
        ####
        a = ET.Element("Work_Env")
        ET.SubElement(a, "wdir", name="wdir").text = self.wdir
        ET.SubElement(a, "idir", name="idir").text = self.idir
        ET.SubElement(a, "tdir", name="tdir").text = self.tdir
        ET.SubElement(a, "odir", name="odir").text = self.odir
        ET.SubElement(a, "WorkEnv", name="WorkEnv").text = self.WorkEnv
        ET.SubElement(a, "backgroundImage", name="backgroundImage").text = self.backgroundImage
        ET.SubElement(a, "gammaCommands", name="gammaCommands").text = self.gammaCommands
        root.extend((a))
        # print("the root is")
        # print(root)
        # Wrtite Pretty XML File
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="")
        print(r"Your created WorkENV: " + xmlstr)
        with open(filename, "w") as f:
            f.write(xmlstr)
            # f.write(xmlstr.encode('utf-8'))
        print("----- Dynamic WorkENV created")


    # def get_wdir(self):
    #     """
    #     I Think this is not useful because were are reading the WorkENV.xml via auxilliary/read_env.py
    #     :return:
    #     """
    #     return self.wdir

    def set_idir(self,idir):
        """
        This is the Function to Set the Import Directory, the Input comes from QMainWindow_{}.py where the Import Directory is Set (BrowseButton)
        The Function Reads in the WorkEnv.xml and changes the idir Parameter and saves it back, all other Parameters are untouched

        :param idir:
        :return:
        """
        print("----- Adding Import Directory to your dynamic WorkENV ")
        print(r"Your Import Directory is: " + idir)
        # TODO SET GUI INPUT -- Working(do double Check) make it pretty
        print("----- Start Adding Import Directory to WorkEnv.xml")
        tree = ET.parse(Environment.WorkEnv)
        # print("Das ist die Struktur des Trees")
        # print(tree)
        root = tree.getroot()
        filename = root[4].text
        #print(root[1].text)
        self.idir = idir
        #print(my_idir)
        root[1].text = str(self.idir)
        #
        #Wrtite Pretty XML File
        # http://ronrothman.com/public/leftbraned/xml-dom-minidom-toprettyxml-and-silly-whitespace/#best-solution
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="",newl='')
        print(r"Your created WorkENV: " + xmlstr)
        with open(filename, "w") as f:
            f.write(xmlstr)
            #f.write(xmlstr.encode('utf-8'))
        print("----- Dynamic WorkENV created")

    # def get_idir(self):
    #     """
    #     This Gets the Class Variable IDIR Blödsinn geht nicht...
    #     :return:
    #     """
    #     #
    #     # tree = ET.parse(r"D:\gammaGUIv2\auxilliary\WorkEnv.xml")
    #     # print("Das ist die Struktur des Trees")
    #     # print(tree)
    #     # root = tree.getroot()
    #     # print(root[1].text)
    #     # wanted_dir = root[1].text
    #     # wanted_dir = str(wanted_dir)

        # return wanted_dir
    def set_odir(self,odir):
        """
        This is the Function to Set the Output Directory, the Input comes from QMainWindow_{}.py where the Output Directory is Set (BrowseButton)
        The Function Reads in the WorkEnv.xml and changes the odir Parameter and saves it back, all other Parameters are untouched
        :param odir:
        :return:
        """
        print("----- Adding Ourput Directory to your dynamic WorkENV ")
        print(r"Your Import Directory is: " + odir)
        self.odir = odir

        print("----- Start Adding Import Directory to WorkEnv.xml")
        tree = ET.parse(Environment.WorkEnv)
        root = tree.getroot()
        filename = root[4].text
        print(root[3].text)
        # my_odir = self.odir
        # print(my_odir)
        root[3].text = str(self.odir)
        # print(root)
        # # print(root[1])
        # print("Was geht gerade")
        # Write Pretty XML File
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="",newl='')
        print(r"Your created WorkENV: " + xmlstr)
        with open(filename, "w") as f:
            f.write(xmlstr)
            # f.write(xmlstr.encode('utf-8'))
        print("----- Dynamic WorkENV created")

    # def get_odir(self):
    #     """
    #     This Gets the Class Variable odir
    #     :return:
    #     """
    #     return self.odir

    def set_tdir(self,tdir):
        """
        This is the Function to Set the Output Directory, the Input comes from QMainWindow_{}.py where the Output Directory is Set (BrowseButton)
        The Function Reads in the WorkEnv.xml and changes the odir Parameter and saves it back, all other Parameters are untouched
        TODO NO manual User Input -> Write Class and Method to do this in the Background -> Implement it ( can be usefull for full automated processing chain e.g. Import S1_TOPS complette Processing
        :param tdir:
        :return:
        """
        print("Hallo, this is the Section where I Want to create the tmp Directory, but right now I'm not implemented ")
        self.tdir = tdir

        print("Start Creating Environment")
        tree = ET.parse(Environment.WorkEnv)
        root = tree.getroot()
        filename = root[4].text
        print(root[2].text)
        my_tdir = self.tdir
        print(my_tdir)
        root[2].text = str(self.tdir)
        print(root)
        # print(root[1])
        print("Was geht gerade")
        # Wrtite Pretty XML File
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="",newl='')
        print(xmlstr)
        with open(filename, "w") as f:
            f.write(xmlstr)
            # f.write(xmlstr.encode('utf-8'))
        print("End XML")

    # def get_tdir(self):
    #     """
    #     This Gets the Class Variable tdir
    #
    #     :return:
    #     """
    #     return self.tdir




if __name__ == '__main__':
    env = Environment()
    print(env)
    print(env.WorkEnv)
    print(env.set_idir)
    t = env.get_idir()
    print(t)