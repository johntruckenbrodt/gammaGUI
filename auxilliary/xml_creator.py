# This Shoud be a xml_creater File
# Usage: Write XML of all GAMMA Main Commands
#############################################
import os
import xml.etree.cElementTree as ET
from xml.dom import minidom
from auxilliary.read_env import ReadEnv

# TODO Implement xml_Creater for PAR Files -> see Script implement_me_to_xml_creator.py

class XMLCreaterGAMMA:
    """
    This is the Class to Create and Read XML Data for or from the Gamma Output Text Files.
    At the moment it Contains:
        - Methods to write and read the GammaCommands.xml
        - Methods to write and read the *PAR.xml Files (shout be implementet today, by Felix)
    """

    def __int__(self, path, filename, args):
        self.filename = filename
        self.path = path
        self.args = args


    def create_XMLGAMMA(self, path, filename, args):
        """
        This Method creates a XML File based on Users Input. It is used to create the GammaCommands.xml.
        This File is on the one side created to track the implementation Status on the other side to
        ensure readable and a easy access to the needed Gamma Commands.
        If you run this Function by its on (in this File) you can easily add a new Gamma Command by adding it to the List
        TODO is there a better Solution?! Make nice Print Commands

        :param filename: string of Filename
        :param path: string of OutputDir
        :param args: List of string Arguments (Name of the Gamma Command)
        :return: File Creation
        """
        self.filename = filename + ".xml"
        print("The Filename is:" + self.filename)
        self.path = path
        self. args = args
        self.outpath = os.path.join(self.path, str(self.filename))

        print(self)
        print("Start Creating XML-File for GAMMA Main Commands")
        print("Initialize GammaCommand.xml")
        root = ET.Element("root")
        ####
        a = ET.Element("GAMMA_COMMANDS")
        for i in range(0,len(self.args)):
            ET.SubElement(a,self.args[i], name=self.args[i]).text = self.args[i]

        root.extend(a)

        # Wrtite Pretty XML File
        xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="") # (indent="" , newl="") If you are Reading a File and Rewriting it
        print(xmlstr)
        print(self.outpath)
        with open(self.outpath, "w") as f:
            f.write(xmlstr)
            #f.write(xmlstr.encode('utf-8'))
        print("End XML")

    def read_XMLGAMMA(self,GammaCommandKey):
        """
        This is the Method to read the GammaCommands.xml. It returns the Name of the Gamma Command.

        :param GammaCommandKey: string of Gamma Command name
        :return: string of GammaCommand
        """

        WorkENV = ReadEnv()
        my_WorkENV =WorkENV.read_env()


        path = my_WorkENV[6]
        #filename = filename +".xml"
        gammacommandkey = GammaCommandKey

        tree = ET.parse(path)
        root = tree.getroot()

        for elem in root.iter(gammacommandkey):
            print(elem.attrib["name"])
            command = elem.attrib["name"]
            #print(type(elem.attrib))
        print(command)

        return command


if __name__ == '__main__':
    """
    Here you can add a new GammaCommand to the GammaCommands.xml Just add the ne Module to the list and run this file
    """
    xml = XMLCreaterGAMMA
    # Create List with all Entries (GammaMain Commands)
    # TODO FINA ALL NECESSARY GAMMA-COMMENTS
    myList = list(["par_S1_SLC",
                   "par_S1_GRD",
                   "SLC_Burst_Corners",
                   "SLC_mosaic_S1_TOPS",
                   "multi_looking"])
    print(myList)
    # RUN HERE
    xml.create_XMLGAMMA(xml, r"D:\gammaGUI\gamma", r"GammaCommands", myList)
    # OR RUN HERE
    #xml.read_XMLGAMMA("par_S1_SLC")

