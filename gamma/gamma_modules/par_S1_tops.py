# Searches for Files for Import to Gamma
# Inheriate readers from gammaGUI
# Adjust these ?!

# import os
# from auxilliary.read_env import ReadEnv
# import xml.etree.cElementTree as ET
# import re
# from auxilliary.read_env import ReadEnv
# from auxilliary.create_args import Args
from gamma.gamma_args.create_gamma_args import GammaArgs
# import argparse
# import sys
import subprocess as sp


# Diese Klasse Repersensiert das S1_TOPS Gamma Module
# Damit wenn ok geklickt die Gamma Prozessierung startet
# Dazu brauche ich :
#   - eine Methode zum erstellen der Argumente
#           -



class ParS1Tops():
    """
    This Class Contains a method to handle the Given Arguments
    from D:\gammaGUIv2\auxilliary\create_args.py  -> Args.create_args_S1_TOPS()

    """

    # def __init__(self):
    #     self.WorkEnv = ""


    def run_par_S1_tops():
        """
        This is the Function to execute the received List of Lists from Args.create_args_S1_TOPS() on the shell
        Therefore subprocess.Popen(args,shell = T) is used
        :return:
        """

        print("------- Start Importing S1_TOPS data to GAMMA ------")
        # Import list of Arguments from ceate_args.py create_args_S1_TOPS
        my_Args = GammaArgs()
        my_args_list = my_Args.create_args_par_S1_SLC()

        # TODO Find out if we need a parser. Good Idea or Bad Idea ?! Right now we need none
        # # Create Parser
        # parser = argparse.ArgumentParser(description="Import S1_TOPS to GAMMA Format")
        # # parser.add_argument('--sys.executable', help='sys.executable help')
        # # parser.add_argument('--sys.argv', help='sys.executable help')
        # parser.add_argument('--S1_TOPS', help='sys.executable help')
        # parser.add_argument('--GammaModule', help='GammaModule help')
        # parser.add_argument('--GeoTIFF', help='GeoTIFF help')
        # parser.add_argument('--annotationXML', help='annotationXML help')
        # parser.add_argument('--calibrationXML', help='calibrationXML help')
        # parser.add_argument('--noiseXML', help='noiseXML help')
        # parser.add_argument('--SLC_Par', help='SLC_Par help')
        # parser.add_argument('--SLC', help='SLC help')
        # parser.add_argument('--TOPS_par', help='TOPS_par help')
        # parser.add_argument('--dtype', help='dtype help')
        # parser.add_argument('--sc_dB', help='dtype help')
        # print(parser)

        #sp.CREATE_NEW_CONSOLE

        print("------- Run Arguments for par_S1_SLC Gamma Command ------")

        for i in range(0, len(my_args_list[0])):
            my_args = my_args_list[0][i] #.split() vllt nötig (has to be tested in the Server)
            print(my_args)
            #sp.run(parser.parse_args(my_args))
            sp.Popen(my_args, shell=True)

        print("------- Create Folders (Basename) and copy specific slc Files tops. par ------")
        # TODO "Clean Up" Create Folders und copy Specific Files there

        for i in range(0, len(my_args_list[1])):
            my_args = my_args_list[1][i] #.split() vllt nötig (has to be tested in the Server)
            print(my_args)
            #sp.run(parser.parse_args(my_args))
            sp.Popen(my_args, shell=True)

        print("------- CREATE XML FILE FOR *.slc.par and *.tops.par ------")

        #TODO Implement XML Creater
        #TODO slc_mosaic_S1_TOPS -> in new Folder
        #TODO Rewrite Script to Object
        #TODO WRITE FUNCTION TO READ XML FILE AND READ ML FACKTOR AND SO ON
        #TODO THNIK OF FURTHER PROCESSING
        #     - automated or "clicky" or both (Check Button ?!)

if __name__ == '__main__':
    #TODO Clean up make it runing from Main (if possible)
    readed = S1TOPS
    print(readed)
    readed.run_S1_TOPS
    print(readed.run_S1_TOPS)



    # my_ENV = ReadEnv()
    # Work_ENV = my_ENV.read_env()
    # readed = S1_TOPS(Work_ENV)
    # readed.module_S1_TOPS(Work_ENV)
    # #readed.module_S1_TOPS(readed)

    print(readed)