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


class ParS1GRD():
    """
    This is the API Class to the Server to process the with Gamma.
    It is used to run the received arguments from create_gamma_args.py
    -----
    Original Code by Stefan, implementation to the Framework by Felix
    -> No tests executed

    """

    def run_par_S1_GRD():
        print("------- Start Importing S1_TOPS data to GAMMA ------")
        # Import list of Arguments from ceate_args.py create_args_S1_TOPS
        my_Args = GammaArgs()
        my_args_list = my_Args.create_args_par_S1_GRD()

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

        #TODO
        # Implement further Gamma Functions
        # Write and Implement Funcktion to Read the par.xml Data e.g. extract multilooking factors
        # Think about the further Processing, fully automated or "clicky" or both (Combine with Check Buttons?!)
        # Write and implement a Class and Method to Import a DEM

if __name__ == '__main__':
    #TODO Clean up make it runing from Main (if possible)
    readed = ParS1GRD
    print(readed)
    readed.run_par_S1_GRD()
    print(readed.run_par_S1_GRD())



    # my_ENV = ReadEnv()
    # Work_ENV = my_ENV.read_env()
    # readed = S1_TOPS(Work_ENV)
    # readed.module_S1_TOPS(Work_ENV)
    # #readed.module_S1_TOPS(readed)

    print(readed)