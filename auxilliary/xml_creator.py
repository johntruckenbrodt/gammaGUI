# Author: Stefan Werner
# create_XML_FROM_PAR_SLC_SLCTOPS : Core Code Stefan Werner / Implementation Felix Behrendt
import os
import glob
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

    def create_XML_FROM_PAR_SLC_SLCTOPS(self):
        """
        Original Code by Stefan, implementation to Framework by Felix
        TODO Integrate to Copy Command -> tidy folder Structure after Processing (Implementation not tested on the Server)
        :return:
        """

        # Set/Get Wdir
        my_dir = ReadEnv()
        WorkEnv = my_dir.read_env()

        # Create Import Dir
        idir = WorkEnv[1]

        odir = WorkEnv[3]

        # Set Extensions
        # TODO Pars Arguments?!
        # TODO How to Handle reader.par
        extension = ("slc.par", "slc.tops_par")
        # extension = ".tops_par"

        # Create List of Parameter Files (".par,.tops_par") # Each a List

        my_pars = list()
        for i in range(0, len(extension)):
            my_pars.append(glob.glob(idir + '/*' + extension[i]))
        print("______________HERE_____________List of PAR FILES")
        print(my_pars)


        for i in range(0, len(my_pars[0])):

            # Filename and Path  of XML
            filename = my_pars[0][i].replace(".par", "_ISP_PARS.xml")
            filename = odir + "PAR_" + filename.partition(idir)[2]

            # Open corresponding par and top.par
            par = list()
            tops_par = list()
            f = open(my_pars[0][i], 'r')
            for line in f:
                if len(line) == 1:
                    continue
                par.append(line.strip())

            f = open(my_pars[1][i], 'r')
            for line in f:
                if len(line) == 1:
                    continue
                tops_par.append(line.strip())

            # Creat Tuple of File Pairs
            my_par_pairs = (par, tops_par)

            ### Start Splitting in XML Parts

            # Title
            my_titles = (my_par_pairs[0][0], my_par_pairs[1][0])

            # Fields and Names
            # Fields are used to create a Tag?!
            # Names are used to further Processing

            my_fields_par = list()
            my_names_par = list()

            print(my_par_pairs[0])

            for i in range(1, len(my_par_pairs[0])):
                field = my_par_pairs[0][i].split(":", 1)

                my_fields_par.append(field[0])
                my_names_par.append(field[1].strip())

            my_fields_tops_par = list()
            my_names_tops_par = list()

            for i in range(1, len(my_par_pairs[1])):
                field = my_par_pairs[1][i].split(":", 1)
                my_fields_tops_par.append(field[0])
                my_names_tops_par.append(field[1].strip())

            my_fields = (my_fields_par, my_fields_tops_par)  # Finished for XML
            my_names = (my_names_par, my_names_tops_par)  # Used to Extract Values and Units

            # Get Elements and Units
            ########################### PAR Processing ######################
            my_elements_par = list()
            # Title Element
            my_elements_par.append(my_names[0][0])
            # Sensor Element
            my_elements_par.append(my_names[0][1])
            # Add Date Element
            # TODO possible Format
            my_elements_par.append(my_names[0][2])

            import re

            for i in range(3, len(my_names[0])):
                elements = re.findall("^[A-Z0-9\.\+\-e\s\_\:]+", my_names[0][i])
                if elements[0].endswith("H"):
                    elements[0] = elements[0][:-1]
                unit = my_names[0][i].split(elements[0])
                unit = unit[1].strip()
                # elements = filter(None,elements)
                elements = re.sub(" {1,}", " ", elements[0])
                elements = elements.strip()
                ele_uni = [elements, unit]

                my_elements_par.append(ele_uni)

            ######################### TOPS_PAR Processing #####################

            my_elements_tops_par = list()

            # Title Element
            my_elements_tops_par.append(my_names[1][0])

            for i in range(1, len(my_names[1])):
                elements = re.findall("^[A-Z0-9\.\+\-e\s\_\:]+", my_names[1][i])
                if elements[0].endswith("H"):
                    elements[0] = elements[0][:-1]
                unit = my_names[1][i].split(elements[0])
                unit = unit[1].strip()
                # elements = filter(None,elements)
                elements = re.sub(" {1,}", " ", elements[0])
                elements = elements.strip()
                ele_uni = [elements, unit]

                my_elements_tops_par.append(ele_uni)

            my_elements = (my_elements_par, my_elements_tops_par)

            print("STOP")

            ########################################################################################
            ###### START XML CREATION ##############################################################
            ########################################################################################

            print("Create XML")
            ##########
            # XML
            # https://stackoverflow.com/questions/3605680/creating-a-simple-xml-file-using-python,
            # https://lxml.de/tutorial.html
            # https://stackoverflow.com/questions/9971538/what-are-the-arguments-of-elementtree-subelement-used-for
            # https://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree/
            ##########

            import xml.etree.cElementTree as ET
            root = ET.Element("root")
            ####
            a = ET.Element("ISP_IPF_PAR")
            ET.SubElement(a, "PAR_File").text = my_titles[0]
            ET.SubElement(a, my_fields[0][0]).text = my_elements[0][0]
            ET.SubElement(a, my_fields[0][1]).text = my_elements[0][1]
            ET.SubElement(a, my_fields[0][2]).text = my_elements[0][2]

            for i in range(3, len(my_fields[0])):
                ET.SubElement(a, my_fields[0][i], unit=my_elements[0][i][1]).text = my_elements[0][i][0]

            # a_sub = ET.SubElement(a,my_fields[3],unit=my_elements[3][1]).text = my_elements[3][0]
            # a_sub2 = ET.SubElement(a_sub,"Unit").text = my_elements[3][1]

            ####
            b = ET.Element("ISP_IPF_TOPS_PAR")
            ET.SubElement(b, "TOPS_PAR_File").text = my_titles[1]
            ET.SubElement(b, my_fields[1][0]).text = my_elements[1][0]
            for i in range(1, len(my_fields[1])):
                ET.SubElement(b, my_fields[1][i], unit=my_elements[1][i][1]).text = my_elements[1][i][0]

            ######################################
            root.extend((a, b))

            # Wrtite Pretty XML File
            from xml.dom import minidom

            xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
            with open(filename, "w") as f:
                f.write(xmlstr)
                # f.write(xmlstr.encode('utf-8'))

            print("End XML")


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

