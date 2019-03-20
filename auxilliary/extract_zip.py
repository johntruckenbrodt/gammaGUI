#!/usr/bin/env python

"""
Python 2.7.15 |Anaconda, Inc.| (default, May  1 2018, 18:37:09) [MSC v.1500 64 bit (AMD64)]
Python 2.7.15 |Anaconda, Inc.| (default, May  1 2018, 18:37:09) [MSC v.1500 64 bit (AMD64)] on win32

Tasks: List Zip Files and extract them into Same Folder (GammaGUI needs *.SAFE Structure)
"""

from auxilliary.environment import Environment
import xml.etree.cElementTree as ET
from auxilliary.read_env import ReadEnv
import os
import zipfile

class ZippedFiles():
    """
    This is the Class for Zipped Files
    At the current Status, this Class contains only one Method to extract *.zip Files (e.g. S1)
    To initialize the WorkENV a instance of ReadEnv is created. The arguments form the read_env() are return to
    the Variable my_WorkENV
    The Class Variables my_WorkENV is a list of the Entries of the WorkEnv.xml (Paths)
    The order is:
        0. wdir
        1. idir
        2. tdir
        3. odir
        4. WorkEnv.xml
        5. backgroundimage
        6. GammaCommands.xml
    """
    try:

        WorkENV = ReadEnv()
        my_WorkENV = WorkENV.read_env()

    except FileNotFoundError:
        print("The File WorkENV.xml does not exists! Please set Your Working Directory\nImport -> Set Working Directory")

    def unzip_files():
        """
        This is the Method of the Class ZippedFiles. It creates a Instance of the Class ZippedFiles.
        From the returned List, idir and odir are read and passed to the Extraction Loop
        TODO further TODO's in gammaGUIv2/gui_windows/QSubWindow_data_extraction.py
        :return:
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

        # # Just Printing the WorkENV
        # for i in range(0,len(args.my_WorkENV)):
        #     print(args.my_WorkENV[i])

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








