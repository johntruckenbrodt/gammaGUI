#!/usr/bin/env python
# Author: Stefan Werner

"""
Python 2.7.15 |Anaconda, Inc.| (default, May  1 2018, 18:37:09) [MSC v.1500 64 bit (AMD64)]
Python 2.7.15 |Anaconda, Inc.| (default, May  1 2018, 18:37:09) [MSC v.1500 64 bit (AMD64)] on win32

Tasks: Create XML-File from *.par, *tops.par
"""
def main():

    # Import Libs
    import os
    import glob
    # import lxml.etree
    # import lxml.builder

    # Set/Get Wdir
    # TODO Get current Path from Enviroment Object ?!
    #wdir = os.path.join(os.getcwd(),"gammaGUI")
    wdir = os.path.join(os.getcwd())

    # Set Extensions
    # TODO Pars Arguments?!
    # TODO How to Handle reader.par
    extension = ("slc.par","slc.tops_par")
    #extension = ".tops_par"

    # Create List of Parameter Files (".par,.tops_par") # Each a List
    my_pars = list()
    for i in range(0,len(extension)):
        my_pars.append(glob.glob(wdir + '/**/*' + extension[i]))
    my_pars

    print(my_pars)

    create_xml(my_pars)

### Create Function to Split Par Fiels to indiviald Parts Prepferation for  XML for Each File and Save to Spectific Folder
# Each XML Should consists of 2 Entries 1 For .par and one for tops.par

"""
my_pars[0][0]
my_pars[1][0]
"""
#my_par_list = my_pars

def create_xml (my_par_list):
    for i in range(0,len(my_par_list[0])):

        # Filename and Path  of XML
        filename = my_par_list[0][i].replace(".par","_ISP_PARS.xml")

        # Open corresponding par and top.par
        par = open(my_par_list[0][i],"r+").read()
        par = par.split("\n", -1)  # Split at each \n
        par = filter(None, par)

        tops_par = open(my_par_list[1][i],"r+").read()
        tops_par = tops_par.split("\n",-1)
        tops_par = filter(None,tops_par)

        # Creat Tuple of File Pairs
        my_par_pairs = (par,tops_par)

        ### Start Splitting in XML Parts

        # Title
        my_titles = (my_par_pairs[0][0],my_par_pairs[1][0])

        # Fields and Names
        # Fields are used to create a Tag?!
        # Names are used to further Processing

        my_fields_par = list()
        my_names_par = list()

        for i in range(1, len(my_par_pairs[0])):
            field = my_par_pairs[0][i].split(":", 1)
            my_fields_par.append(field[0])
            my_names_par.append(field[1].strip())

        my_fields_par
        my_names_par

        my_fields_tops_par = list()
        my_names_tops_par = list()

        for i in range(1, len(my_par_pairs[1])):
            field = my_par_pairs[1][i].split(":", 1)
            my_fields_tops_par.append(field[0])
            my_names_tops_par.append(field[1].strip())

        my_fields_tops_par
        my_names_tops_par

        my_fields = (my_fields_par,my_fields_tops_par) # Finished for XML
        my_names = (my_names_par,my_names_tops_par) # Used to Extract Values and Units

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

        my_elements_par

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
        my_elements_tops_par

        my_elements = (my_elements_par,my_elements_tops_par)

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
            # f.write(xmlstr)
            f.write(xmlstr.encode('utf-8'))

        print("End XML")

if __name__ == '__main__':
    main()

