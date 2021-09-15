# Author: core code Felix Behrendt, implementation Stefan Werner
from PyQt5 import QtWidgets
from auxilliary.environment import Environment

class BrowseDialoge(QtWidgets.QFileDialog):
    """
    This is the Class for the Browse Dialog.
    It should contain all Methods to open a FileDialoge to extract Folder path or Filepath
    Currently it contains only Methods to extract a Folder Path
    Original Code by Felix, implementation by Stefan
    """

    def __init__(self):
        super(BrowseDialoge).__init__(self)

    def browse_function(self):
        """
        This Methods open the FileDialog and writes the selected Folder Path to a Function Variable and uses the
        Environment.set_wdir() to create the wdir Entry in the WorkENV.xml
        :return:
        """
        fd = QtWidgets.QFileDialog()
        print(r"Start Dialog File Search")
        print(fd)
        fname = str(fd.getExistingDirectory(parent=None))
        print(fname)

        #TODO
        # Find a Solution to Show fname
        # in LineEdit of QSubWindow_set_your_working_directory
        # after that press OK Button to run the Function Enviornment.set_wdir(fname) to Create WorkENV.xml
        # at the Moment the Solution is:
        # If you Press the Button in the QBrowseDialog Window the WorkENV.xml is Created,
        # there is no Functionality on the other Buttons. To Close the Window use X

        # Set in Enviroment
        instanz = Environment()
        Environment.wdir = instanz.set_wdir(fname)

class BrowseDialogeInput(QtWidgets.QFileDialog):

    def __int__(self):
        super(BrowseDialoge).__init__(self)

    def browse_function(self):
        """
        This Methods open the FileDialog and writes the selected Folder Path to a Function Variable and uses the
        Environment.set_idir() to create the idir Entry in the WorkENV.xml
        :return:
        """
        fd = QtWidgets.QFileDialog()
        print(r"Start Dialog File Search")
        print(fd)
        fname = str(fd.getExistingDirectory(parent=None))
        print(fname)

        #Set in Enviroment
        instanz = Environment()
        Environment.idir = instanz.set_idir(fname)

class BrowseDialogeTmp(QtWidgets.QFileDialog):

    def __int__(self):
        super(BrowseDialoge).__init__(self)

    def browse_function(self):
        """
        This Methods open the FileDialog and writes the selected Folder Path to a Function Variable and uses the
        Environment.set_tdir() to create the tdir Entry in the WorkENV.xml
        :return:
        """
        fd = QtWidgets.QFileDialog()
        print(r"Start Dialog File Search")
        print(fd)
        fname = str(fd.getExistingDirectory(parent=None))
        print(fname)

        # Set in Enviroment
        instanz = Environment()
        Environment.tdir = instanz.set_tdir(fname)

class BrowseDialogeOdir(QtWidgets.QFileDialog):

    def __int__(self):
        super(BrowseDialoge).__init__(self)

    def browse_function(self):
        """
        This Methods open the FileDialog and writes the selected Folder Path to a Function Variable and uses the
        Environment.set_odir() to create the odir Entry in the WorkENV.xml
        :return:
        """
        fd = QtWidgets.QFileDialog()
        print(r"Start Dialog File Search")
        print(fd)
        fname = str(fd.getExistingDirectory(parent=None))
        print(fname)

        # Set in Enviroment
        instanz = Environment()
        Environment.odir = instanz.set_odir(fname)
        print(Environment.odir)