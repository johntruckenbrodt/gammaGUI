# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\gammaGUIv2\gammaGUIv2\Qt_Export\QSubWindow_set_your_working_directory.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from auxilliary.environment import Environment
from gammaGUIv2.gui_windows.QBrowseDialoge import BrowseDialoge

class Ui_QSubWindow_set_your_working_directory(object):
    """
        This is the Class of the Set Your Workin Directory Window
    """
    def setupUi(self, QSubWindow_set_your_working_directory):
        """
        This the the Setup Method for the UI

        IDEA -> Set Size of SubWindows in environment.Environment

        :param MainWindow:
        :return:
        """
        # Set Up window
        QSubWindow_set_your_working_directory.setObjectName("QSubWindow_set_your_working_directory")
        QSubWindow_set_your_working_directory.resize(600, 141)
        self.verticalLayout = QtWidgets.QVBoxLayout(QSubWindow_set_your_working_directory)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalWidget_8 = QtWidgets.QWidget(QSubWindow_set_your_working_directory)
        self.horizontalWidget_8.setObjectName("horizontalWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalWidget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.label_5 = QtWidgets.QLabel(self.horizontalWidget_8)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_7.addWidget(self.horizontalWidget_8)
        self.verticalWidget_5 = QtWidgets.QWidget(QSubWindow_set_your_working_directory)
        self.verticalWidget_5.setObjectName("verticalWidget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalWidget_9 = QtWidgets.QWidget(self.verticalWidget_5)
        self.horizontalWidget_9.setObjectName("horizontalWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalWidget_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)

        """
        2.Step of Implementation
        -> Connect Buttons in the this SubWindow with our Functions
        -> e.g Line: Printing os.getwd() in Line
        -> eg. BrowseButton: Open File Dialoge Window -> Browse to Folder -> Pass this to enviroment.Enviroment as WDIR
        -> read our Lineinput: -> Pass this to environment.Environment as WDIR
        -> ButtonBOX:
            - OK -> Pass Browsed Direktory to environment.ENvironment
            - Cancel -> Quit this Window
                      
        Example of Implementation:
        self.pushButton_3.setObjectName("pushButton_3")
        
        
        """

        # Input Line Dialog
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalWidget_9)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText(Environment.wdir)

        self.horizontalLayout_9.addWidget(self.lineEdit_3)

        # Browse Button
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalWidget_9)
        self.pushButton_3.setObjectName("pushButton_3")
        #self.pushButton_3.triggerd.connect(BrowseDialoge.browse_function)
        self.pushButton_3.clicked.connect(BrowseDialoge.browse_function)


        self.horizontalLayout_9.addWidget(self.pushButton_3)
        self.horizontalWidget_14 = QtWidgets.QWidget(self.horizontalWidget_9)
        self.horizontalWidget_14.setObjectName("horizontalWidget_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalWidget_14)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)

        # ButtonBox (Ok and Cancel)
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.horizontalWidget_14)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")

        self.horizontalLayout_14.addWidget(self.buttonBox_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.horizontalLayout_9.addWidget(self.horizontalWidget_14)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.verticalLayout_4.addWidget(self.horizontalWidget_9)
        self.verticalLayout_7.addWidget(self.verticalWidget_5)
        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.retranslateUi(QSubWindow_set_your_working_directory)
        QtCore.QMetaObject.connectSlotsByName(QSubWindow_set_your_working_directory)

    def retranslateUi(self, QSubWindow_set_your_working_directory):
        _translate = QtCore.QCoreApplication.translate
        QSubWindow_set_your_working_directory.setWindowTitle(_translate("QSubWindow_set_your_working_directory", "Dialog"))
        self.label_5.setText(_translate("QSubWindow_set_your_working_directory", "Select your Working Directory"))
        self.pushButton_3.setToolTip(_translate("QSubWindow_set_your_working_directory", "<html><head/><body><p>Browse to Working Directory</p></body></html>"))
        self.pushButton_3.setText(_translate("QSubWindow_set_your_working_directory", "Browse"))
        self.buttonBox_2.setToolTip(_translate("QSubWindow_set_your_working_directory", "<html><head/><body><p>Press Ok to set your Working Directory</p><p>Press Cancel to Quit Dialog </p></body></html>"))

    def create_Ui_QSubWindow_set_your_working_directory(self):
        QSubWindow_set_your_working_directory = QtWidgets.QDialog()
        ui = Ui_QSubWindow_set_your_working_directory()
        ui.setupUi(QSubWindow_set_your_working_directory)
        QSubWindow_set_your_working_directory.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QSubWindow_set_your_working_directory = QtWidgets.QDialog()
    ui = Ui_QSubWindow_set_your_working_directory()
    ui.setupUi(QSubWindow_set_your_working_directory)
    QSubWindow_set_your_working_directory.show()
    sys.exit(app.exec_())

