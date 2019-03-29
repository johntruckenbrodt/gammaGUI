# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from auxilliary.environment import Environment
from gammaGUIv2.gui_windows.QBrowseDialoge import *
from auxilliary.extract_zip import ZippedFiles

class Ui_QSubWindow_data_extraction(object):
    """
    This is the QSubWindow Class of the Date Extraction Window. This Class contains the hole Layout of the QSubWindow
    including all Buttons witch can be occupied with Functionality.
    Here you can link the Button with Function via accepted.connect() or clicked.connect():
        - writing the WorkEnv.xml for Input and Output
        - starting a Script when pressing ok eg. extraction zips
   """
    def setupUi(self, QSubWindow_data_extraction):
        """
        This the the Setup Method for the UI.
        TODO Add functionality to ALL Buttons -> further details for the TODO's see below
        :param QSubWindow_data_extraction:
        :return:
        """

        ###
        # Setup for QSubwindow_{}
        ###
        QSubWindow_data_extraction.setObjectName("QSubWindow_data_extraction")
        QSubWindow_data_extraction.resize(685, 255)
        self.verticalLayout = QtWidgets.QVBoxLayout(QSubWindow_data_extraction)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalWidget_8 = QtWidgets.QWidget(QSubWindow_data_extraction)
        self.horizontalWidget_8.setObjectName("horizontalWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalWidget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)

        ###
        # CheckBOX: Select all Files
        ###
        #TODO
        # Write and implement a Method to read this Checkbox and automatically select all Files in Folder, when pressing OK.
        # I think this has to be done with Signals and in the auxilliary/extract_zip.py, If statement
        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalWidget_8)
        self.checkBox_3.setObjectName("checkBox_3")


        self.horizontalLayout_8.addWidget(self.checkBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalWidget = QtWidgets.QWidget(self.horizontalWidget_8)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        ###
        # RadioBOX: *.rar Button
        ###
        # TODO
        #  Write and implement a Method to read this Checkbox and automatically select the *rar Files in Folder, when pressing OK.
        #  I think this has to be done with Signals and in the auxilliary/extract_zip.py, If statement
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalWidget)
        self.radioButton_6.setObjectName("radioButton_6")

        self.verticalLayout_5.addWidget(self.radioButton_6)

        ###
        # RadioBOX: '.zip Button
        ###
        # TODO
        #  Write and implement a Method to read this Checkbox and automatically select the *zip Files in Folder, when pressing OK.
        #  I think this has to be done with Signals and in the auxilliary/extract_zip.py, If statement
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalWidget)
        self.radioButton_5.setObjectName("radioButton_5")

        self.verticalLayout_5.addWidget(self.radioButton_5)
        self.horizontalLayout_8.addWidget(self.verticalWidget)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)

        ###
        # CheckBOX: Select Files (Period of time)
        ###
        # TODO
        #  Write and implement a Method to read out this Checkbox for the Start Date for a Start Stop Search Function.
        #  I think this has to be done with Signals and in the auxilliary/extract_zip.py, If statement and one additonal Script for pattern Search placed in auililary.<name>
        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalWidget_8)
        self.checkBox_4.setObjectName("checkBox_4")

        self.horizontalLayout_8.addWidget(self.checkBox_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)

        ###
        # DateEdit Start Date
        ###
        self.dateEdit_3 = QtWidgets.QDateEdit(self.horizontalWidget_8)
        self.dateEdit_3.setObjectName("dateEdit_3")

        self.horizontalLayout_8.addWidget(self.dateEdit_3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.label_5 = QtWidgets.QLabel(self.horizontalWidget_8)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem5)

        ###
        # DateEdit End Date
        ###
        # TODO
        #  Write and implement a Method to read out this Checkbox for the End Date for a Start Stop Search Function.
        #  I think this has to be done with Signals and in the auxilliary/extract_zip.py, If statement and one additonal Script for pattern Search placed in auililary.<name>
        self.dateEdit_4 = QtWidgets.QDateEdit(self.horizontalWidget_8)
        self.dateEdit_4.setObjectName("dateEdit_4")

        self.horizontalLayout_8.addWidget(self.dateEdit_4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.label_6 = QtWidgets.QLabel(self.horizontalWidget_8)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_7.addWidget(self.horizontalWidget_8)
        self.verticalWidget_5 = QtWidgets.QWidget(QSubWindow_data_extraction)
        self.verticalWidget_5.setObjectName("verticalWidget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalWidget_9 = QtWidgets.QWidget(self.verticalWidget_5)
        self.horizontalWidget_9.setObjectName("horizontalWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalWidget_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)

        ###
        # LineEdit Input Folder
        ###
        # TODO
        #  Make a New Placeholder, i think it would be more sufficient to Take the Placeholder from auxilliary/read_env.py.
        #  For this there should be a method to check if WorkEnv.xml exists and if not take it from Environment.xy
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalWidget_9)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText(Environment.wdir)

        self.horizontalLayout_9.addWidget(self.lineEdit_3)

        ###
        # PushButton Browse Button Input Folder
        ###
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalWidget_9)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(BrowseDialogeInput.browse_function)


        self.horizontalLayout_9.addWidget(self.pushButton_3)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.verticalLayout_4.addWidget(self.horizontalWidget_9)
        self.horizontalWidget_10 = QtWidgets.QWidget(self.verticalWidget_5)
        self.horizontalWidget_10.setObjectName("horizontalWidget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalWidget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem10)

        ###
        # LineEdit Output Folder
        ###
        # TODO
        #  Make a New Placeholder, i think it would be more sufficient to Take the Placeholder from auxilliary/read_env.py.
        #  For this there should be a method to check if WorkEnv.xml exists and if not take it from Environment.xy
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalWidget_10)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setPlaceholderText(Environment.odir)

        self.horizontalLayout_10.addWidget(self.lineEdit_4)

        ###
        # PushButton Browse Button Output Folder
        ###
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalWidget_10)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(BrowseDialogeOdir.browse_function)

        self.horizontalLayout_10.addWidget(self.pushButton_4)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.verticalLayout_4.addWidget(self.horizontalWidget_10)
        self.verticalLayout_7.addWidget(self.verticalWidget_5)
        self.horizontalWidget_14 = QtWidgets.QWidget(QSubWindow_data_extraction)
        self.horizontalWidget_14.setObjectName("horizontalWidget_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalWidget_14)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem12)

        ###
        # ProgressBar
        ##
        # TODO
        #  Write Class for ProgressBar, with Method to count the Process (count Files/100 refresh ... see google).
        #  Has to be goggled how do to this
        self.progressBar_2 = QtWidgets.QProgressBar(self.horizontalWidget_14)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")

        self.horizontalLayout_14.addWidget(self.progressBar_2)

        ###
        # ButtonBox OK, CANCEL
        ###
        #TODO
        #  Close Window when Cancel is pressedW
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.horizontalWidget_14)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        # RUN FUNCTION auxiliary.extract_zip.py When Pressing OK
        self.buttonBox_2.accepted.connect(ZippedFiles.unzip_files)


        self.horizontalLayout_14.addWidget(self.buttonBox_2)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.verticalLayout_7.addWidget(self.horizontalWidget_14)
        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.retranslateUi(QSubWindow_data_extraction)
        QtCore.QMetaObject.connectSlotsByName(QSubWindow_data_extraction)

    def retranslateUi(self, QSubWindow_data_extraction):
        """
        This is the Method to rename every Entry in the Window.
        If you want to Change Names DO IT HERE
        :param QSubWindow_data_extraction:
        :return:
        """
        _translate = QtCore.QCoreApplication.translate
        QSubWindow_data_extraction.setWindowTitle(_translate("QSubWindow_data_extraction", "Dialog"))
        self.checkBox_3.setToolTip(_translate("QSubWindow_data_extraction", "<html><head/><body><p>Selects all Files in the Import Folder</p></body></html>"))
        self.checkBox_3.setText(_translate("QSubWindow_data_extraction", "Select all Files"))
        self.radioButton_6.setToolTip(_translate("QSubWindow_data_extraction", "<html><head/><body><p>Select *.rar Data</p></body></html>"))
        self.radioButton_6.setText(_translate("QSubWindow_data_extraction", "*.rar"))
        self.radioButton_5.setToolTip(_translate("QSubWindow_data_extraction", "<html><head/><body><p>Select *.zip Data</p></body></html>"))
        self.radioButton_5.setText(_translate("QSubWindow_data_extraction", "*.zip"))
        self.checkBox_4.setToolTip(_translate("QSubWindow_data_extraction", "<html><head/><body><p>Check to Select Start and End Date of File Import</p></body></html>"))
        self.checkBox_4.setText(_translate("QSubWindow_data_extraction", "Select Files (Period of time)"))
        self.dateEdit_3.setToolTip(_translate("QSubWindow_data_extraction", "<html><head/><body><p>Select Start Date</p></body></html>"))
        self.label_5.setText(_translate("QSubWindow_data_extraction", "Start Date"))
        self.dateEdit_4.setToolTip(_translate("QSubWindow_data_extraction", "<html><head/><body><p>Select End Date</p></body></html>"))
        self.label_6.setText(_translate("QSubWindow_data_extraction", "End Date"))
        self.pushButton_3.setToolTip(_translate("QSubWindow_data_extraction", "<html><head/><body><p>Browse to Import Folder</p></body></html>"))
        self.pushButton_3.setText(_translate("QSubWindow_data_extraction", "Browse"))
        self.pushButton_4.setToolTip(_translate("QSubWindow_data_extraction", "<html><head/><body><p>Browse to Output Folder</p></body></html>"))
        self.pushButton_4.setText(_translate("QSubWindow_data_extraction", "Browse"))
        self.buttonBox_2.setToolTip(_translate("QSubWindow_data_extraction", "<html><head/><body><p>Press Ok to Start Extraction</p><p>Press Cancel to Quit Dialog</p></body></html>"))

    def create_Ui_QSubWindow_data_extraction(self):
        """
        This is the Method to Open the QSubWindow from the QMainWindow. This has to called from there.
        :return:
        """
        QSubWindow_data_extraction = QtWidgets.QDialog()
        ui = Ui_QSubWindow_data_extraction()
        ui.setupUi(QSubWindow_data_extraction)
        QSubWindow_data_extraction.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QSubWindow_data_extraction = QtWidgets.QDialog()
    ui = Ui_QSubWindow_data_extraction()
    ui.setupUi(QSubWindow_data_extraction)
    QSubWindow_data_extraction.show()
    sys.exit(app.exec_())

