# This Shoud be a xml_creater File
# Usage: Write XML of all GAMMA Main Commands
#############################################
import os
import xml.etree.cElementTree as ET
from xml.dom import minidom
from auxilliary.read_env import ReadEnv

# TODO Fit in ENVIROMENT -> The Arguments -> Start of Programm -> initialize GammaCommand.xml
#  Dont know what i thought here, first you can ignore this

# TODO Implement xml_Creater for PAR Files -> see Script Stefan

class XMLCreaterGAMMA:
    """
    This Class Contains:
    - Method to Create A XML FIle Based on USER INPUT
        - Usage: Build YOUR XML e.g. All NAMES for GAMMA MODULES e.g. par_S1_SLC, par_S1_GRD
        - Run this File as main() -> Implement new Gamma Module command -> also useful for status Documentation
    - Method to Read the GammaCommands.xml and Select a Argument by it's name (Same name as in GammaSoftware eg. par_S1_SLC
    """

    def __int__(self, path, filename, args):
        self.filename = filename
        self.path = path
        self.args = args


    def create_XMLGAMMA(self, path, filename, args):
        """
        This Function creates a XML File based on the Inputparameter
        Run this in the main() of this Window (TODO possibly find better solution?!)
        TODO make nice print Commands
        :param filename: Name of XML File
        :param path: OutputDir
        :param args: List of Arguments(str) for the Entries in XML File
        :return:
        """
        self.filename = filename + ".xml"
        print("The Filename is:" + self.filename)
        self.path = path
        self. args = args
        self.outpath = os.path.join(self.path, str(self.filename))

        print(self)
        print("Start Creating XML-File for GAMMA Main Commands")
        print("Initalize GammaCommand.xml")
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
        This Function reads the GammaCommands.xml File and returns the searched name of the Entry.
        While GammaCommandKey is the Search Term, as well as the original Name of the GammaModule
        :param GammaCommandKey:
        :return:
        """

        WorkENV = ReadEnv()
        my_WorkENV =WorkENV.read_env()


        path = my_WorkENV[6]
        #filename = filename +".xml"
        gammacommandkey = GammaCommandKey

        print("Read GammaCommands.xml")

        # IDEA: Write on Entry in Enviroment where all the Arguments[in the correct order] are Stored we need for GammaProcessing
        #       - Therefore we need a Method to Create This String
        #           - Therefore we need more methods to create the SubElements of the String
        tree = ET.parse(path)
        print("Das ist die Struktur des Trees")
        print(tree)
        root = tree.getroot()
        print(root)
        print(root.attrib)
        # for child in root:
        #     print(child.tag, child.attrib)

        for elem in root.iter(gammacommandkey):
            print(elem.attrib["name"])
            command = elem.attrib["name"]
            #print(type(elem.attrib))
        print(command)

        return command


if __name__ == '__main__':
    """
    Run this to add a new GammaCommandKey to the GammaCommands.xml File
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

