#!/usr/bin/env python
import os
import xml.etree.cElementTree as ET
from xml.dom import minidom

class Environment:

    """
    This it the Environment class. Here are all Information are stored which are essential to initialize the GUI.
    Furthermore it Contains Methods to initialize and rewrite the WorkENV.xml. It also can be called "Entry Point".

    At the current Status:
        - if the  WorkEnv.xml does not exists:
            - It has to be created via QSubWindow_set_your_working_directory (Browse button)
        - if the WorkEnv.xml exists:
            - It is read with the stored information
    #TODO possibily change all "/" to "\\" -> good be a good idea for better UNIX/WINDOWS compatibility


    :var wdir: path of current Working Directory
    :var idir: Placeholder for Import Directory (later we are working with the WorkENV.xml)
    :var odir: Placeholder Output Directory
    :var tdir: Placeholder Tmp Directory
    :var backgroundImage: path to the BackgroundImage of the GUI
    :var gammaCommands:  path to gammaCommands.xml

    """
    # Define Class Variables
    # TODO
    #  IDEA: Check if WorkENV.xml exists and set this Values. If not set these.
    #       -> possibly my cause Problems
    wdir = os.path.join(os.getcwd())
    idir = "ImportDir"
    odir = "OutputDir"
    tdir = "TempDir"
    WorkEnv = os.path.join(os.getcwd(), "auxilliary", "WorkEnv.xml")
    backgroundImage = os.path.join(os.getcwd(), "gammaGUIv2", "gui_images", "background.jpg")
    gammaCommands = os.path.join(os.getcwd(), "gamma", "GammaCommands.xml")

    def set_wdir(self,wdir):
        """
        This is the Method to set the initial Working Directory. Furthermore it creates the WorkENV.xml
        :param wdir: path of Working Directory
        :return: Writes the initial WorkENV.xml
        """
        # TODO
        #  Change connection from QBrowseDialoge to QSubWindow_set_your_working_directory
        #  IDEA is:
        #   - When pressing "Select Folder" in the QBrowseDialoge pass this path to the Line in the QSubWindow_set_your_working_directory
        #   - from this Line the Path should be read and this Method should be executed when pressing OK

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
        # Write Pretty XML File
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="")
        print(r"Your created WorkENV: " + xmlstr)
        with open(filename, "w") as f:
            f.write(xmlstr)
            # f.write(xmlstr.encode('utf-8'))
        print("----- Dynamic WorkENV created")


    def set_idir(self,idir):
        """
        This is the Method to set the Import Directory.
        Therefore the WorkENV.xml is read, the Entry for idir is changed and wrote back to the file

        :param idir: Path to Import Directory
        :return: rewrote WorkENV.xml
        """
        print("----- Adding Import Directory to your dynamic WorkENV ")
        print(r"Your Import Directory is: " + idir)
        # TODO SET GUI INPUT -- Working(do double Check) make it pretty
        print("----- Start Adding Import Directory to WorkEnv.xml")
        tree = ET.parse(Environment.WorkEnv)
        root = tree.getroot()
        filename = root[4].text
        self.idir = idir
        root[1].text = str(self.idir)
        #
        #Write Pretty XML File
        # http://ronrothman.com/public/leftbraned/xml-dom-minidom-toprettyxml-and-silly-whitespace/#best-solution
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="",newl='')
        print(r"Your created WorkENV: " + xmlstr)
        with open(filename, "w") as f:
            f.write(xmlstr)
            #f.write(xmlstr.encode('utf-8'))
        print("----- Dynamic WorkENV created")

    def set_odir(self,odir):
        """
        This is the Method to set the Output Directory.
        Therefore the WorkENV.xml is read, the Entry for odir is changed and wrote back to the file
        :param odir: Path to Output Directory
        :return: rewrote WorkENV.xml
        """
        print("----- Adding Output Directory to your dynamic WorkENV ")
        print(r"Your Import Directory is: " + odir)
        self.odir = odir
        print("----- Start Adding Import Directory to WorkEnv.xml")
        tree = ET.parse(Environment.WorkEnv)
        root = tree.getroot()
        filename = root[4].text
        print(root[3].text)
        root[3].text = str(self.odir)
        # Write Pretty XML File
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="",newl='')
        print(r"Your created WorkENV: " + xmlstr)
        with open(filename, "w") as f:
            f.write(xmlstr)
            # f.write(xmlstr.encode('utf-8'))
        print("----- Dynamic WorkENV created")

    def set_tdir(self,tdir):
        """
        This is the Method to set the Tmp Directory.
        Therefore the WorkENV.xml is read, the Entry for tdir is changed and wrote back to the file

        :param tdir: Path to Tmp Directory
        :return: rewrote WorkENV.xml
        """
        self.tdir = tdir
        print("Start Creating Environment")
        tree = ET.parse(Environment.WorkEnv)
        root = tree.getroot()
        filename = root[4].text
        print(root[2].text)
        my_tdir = self.tdir
        print(my_tdir)
        root[2].text = str(self.tdir)
        # Write Pretty XML File
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="",newl='')
        print(xmlstr)
        with open(filename, "w") as f:
            f.write(xmlstr)
            # f.write(xmlstr.encode('utf-8'))
        print("End XML")


if __name__ == '__main__':
    env = Environment()
    print(env)
    print(env.WorkEnv)
    print(env.set_idir)
    t = env.get_idir()
    print(t)