#!/usr/bin/env python
# Author: Stefan Werner
from auxilliary.read_env import ReadEnv
import os
import zipfile

class ZippedFiles():
    """
    This is the Class for Zipped Files. It Contains a Method to read in all *zip Files in one Folder
    and extract them to the same or another.
    """
    try:
        """
        Checks if the WorkENV.xml exists
        """

        WorkENV = ReadEnv()
        my_WorkENV = WorkENV.read_env()

    except FileNotFoundError:
        print("The File WorkENV.xml does not exists! Please set Your Working Directory\nImport -> Set Working Directory")

    def unzip_files():
        """
        This is the Method to extract Zip Files.
        Therefore the WorkEnv.xml is read the Folder Path are extracted.
        After this the Folder is searched for *.zip Files, these are extracted.

        :return: Extracted *zip Files in the Output Path
        """
        WorkENV = ReadEnv()
        args = WorkENV.read_env()
        print(args)

        # Create Instance of ZippedFiles
        #args = ZippedFiles()

        # Get idir
        idir = args[1]
        print("The Import Directory is:" + idir)

        odir = args[3]
        print("The Output Directory is:" + odir)

        # TODO
        #  Set up Check if Extention is *zip, *rar -> see gammaGUIv2/gui_windows/QSubWindow_data_extraction.py
        extension = ".zip"
        print("The Selected Extension is:" + extension)

        # try:
        #     import os, zipfile
        # except ImportError:
        #     # Try to install it automatically
        #     # https://stackoverflow.com/questions/46419607/how-to-automatically-install-required-packages-from-a-python-script-as-necessary
        #     print('Please install {os} and {zipfile} via pip install'.format(os='os',
        #                                                                      zipfile='zipfile'))  # Keine Print Funktion in Python 3?! für format!?

        print('-- Start unzipping --')
        for i in os.listdir(idir):  # loop through items in dir
            print(os.listdir(idir))
            if i.endswith(extension):  # check for ".zip" extension
                file_name = os.path.join(idir,i)  # get full path of files
                print(file_name)
                zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
                zip_ref.extractall(odir)  # extract file to odir
                zip_ref.close()  # close file
                print('File: {file} -- successfully extracted --'.format(file=i))
        print("-- Unzipping finished --")


if __name__ == '__main__':

    #TODO
    # Clean up HERE
    args = ZippedFiles()
    wdir = args.my_WorkENV[1]
    print(wdir)
    extension = ".zip"
    print(extension)


    print('-- Start unzipping --')
    for i in range(0, len(args.my_WorkENV)):
        print(args.my_WorkENV[i])

    # Set wdir and extension
     # String CWD
    extension = ".zip"  # String Extension

    for i in os.listdir(wdir):  # loop through items in dir
        print(wdir)
        if i.endswith(extension):  # check for ".zip" extension
            file_name = os.path.join(wdir,i)  # get full path of files
            print(file_name)
            zip_ref = zipfile.ZipFile(file_name)  # create zipfile object
            print(zip_ref)
            zip_ref.extractall(wdir)  # extract file to dir
            zip_ref.close()  # close file
            print('File: {file} -- successfully extracted --'.format(file=i))

    print("-- Unzipping finished --")








