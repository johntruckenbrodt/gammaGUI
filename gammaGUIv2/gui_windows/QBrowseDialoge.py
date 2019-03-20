from PyQt5 import QtWidgets
from auxilliary.environment import Environment

class BrowseDialoge(QtWidgets.QFileDialog):

    def __init__(self):
        super(BrowseDialoge).__init__(self)

    def browse_function(self):
        """
        Create Browser Window
        - Create Entry in Environment for Wdir

        :return: String of browsed path
        """
        fd = QtWidgets.QFileDialog()
        print(r"Start Dialog File Search")
        print(fd)
        fname = str(fd.getExistingDirectory(parent=None)).replace(r'/', r'\\')
        print(fname)

        #TODO rewrite Method to parse it to Line in Window

        # Set in Enviroment
        instanz = Environment()
        Environment.wdir = instanz.set_wdir(fname)

class BrowseDialogeInput(QtWidgets.QFileDialog):

    def __int__(self):
        super(BrowseDialoge).__init__(self)

    def browse_function(self):
        """
        Create Browser Window
        - Create Entry in Environment for Idir

        :return: String of browsed path
        """
        fd = QtWidgets.QFileDialog()
        print(r"Start Dialog File Search")
        print(fd)
        fname = str(fd.getExistingDirectory(parent=None)).replace(r'/', r'\\')
        print(fname)

        #Set in Enviroment
        instanz = Environment()
        Environment.idir = instanz.set_idir(fname)
class BrowseDialogeTmp(QtWidgets.QFileDialog):

    def __int__(self):
        super(BrowseDialoge).__init__(self)

    def browse_function(self):
        """
        Create Browser Window
        - Create Entry in Environment for tdir

        :return: String of browsed path
        """
        fd = QtWidgets.QFileDialog()
        print(r"Start Dialog File Search")
        print(fd)
        fname = str(fd.getExistingDirectory(parent=None)).replace(r'/', r'\\')
        print(fname)

        # Set in Enviroment
        instanz = Environment()
        Environment.tdir = instanz.set_tdir(fname)
class BrowseDialogeOdir(QtWidgets.QFileDialog):

    def __int__(self):
        super(BrowseDialoge).__init__(self)

    def browse_function(self):
        """
        Create Browser Window
        - Create Entry in Environment for tdir

        :return: String of browsed path
        """
        fd = QtWidgets.QFileDialog()
        print(r"Start Dialog File Search")
        print(fd)
        fname = str(fd.getExistingDirectory(parent=None)).replace(r'/', r'\\')
        print(fname)

        # Set in Enviroment
        instanz = Environment()
        Environment.odir = instanz.set_odir(fname)
        print(Environment.odir)