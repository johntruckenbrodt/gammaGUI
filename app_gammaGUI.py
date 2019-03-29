import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from gammaGUIv2.gui_windows.QMainWindow import Ui_MainWindow

def main():
    """
    This is the Main Application for the gammaGUIv2
    Run this Script to Start the GUI
    :return:
    """

    #My_Environment = Environment()
    app = QApplication(sys.argv)
    app.setStyle("Fusion") #Depends on Platform
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()