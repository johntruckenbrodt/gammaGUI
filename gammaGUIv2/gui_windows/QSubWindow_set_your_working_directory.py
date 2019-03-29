# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from auxilliary.environment import Environment
from gammaGUIv2.gui_windows.QBrowseDialoge import BrowseDialoge


class Ui_QSubWindow_set_your_working_directory(object):
    """
    This is the QSubWindow Class. This class contains the hole Layout of the QSubWindow_set_your_working_directory.
    This file is executed over the triggered.connect() from the QMainWindow.
    Here we can add Functionality to the Buttons via clicked.connect()
    """

    def setupUi(self, QSubWindow_set_your_working_directory):
        """
        TThis the the Setup Method for the UI
        :param MainWindow:
        :return:
        """

        ###
        # Set up for QSubWindow_set_your_working_directory
        ###
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
        Now we are ready to link the Button with a Function via clicked.connect()        
        -> Connect Buttons with another Window
            self.pushButton_3.setObjectName("pushButton_3")
            self.pushButton_3.clicked.connect(BrowseDialoge.browse_function)
        
        -> Set Placeholder in Line
            self.lineEdit_3.setPlaceholderText(Environment.wdir)
        
        -> How to Activate the ButtonBox see: QSubWindow_data_extraction
        """
        ###
        # LineEdit: Working dir
        ###
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalWidget_9)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setPlaceholderText(Environment.wdir)

        self.horizontalLayout_9.addWidget(self.lineEdit_3)

        ###
        # Browse Button:
        ###
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalWidget_9)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(BrowseDialoge.browse_function)

        self.horizontalLayout_9.addWidget(self.pushButton_3)
        self.horizontalWidget_14 = QtWidgets.QWidget(self.horizontalWidget_9)
        self.horizontalWidget_14.setObjectName("horizontalWidget_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalWidget_14)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem3)

        ###
        # ButtonBox (Ok and Cancel)
        ###
        # TODO Read out line String and Set Wdir in Environment, when press OK
        # TODO -- DOUBLE TROUBLE --- with browser, see to todo there -> rweite to parese to line -> and Set Enviroment with OK
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.horizontalWidget_14)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")

        # self.buttonBox_2.accepted.connect(self.buttonBox_2.closeEvent)
        # self.buttonBox_2.accepted.connect(self.accept)
        # self.buttonBox_2.rejected.connect(self.reject)
        # self.accepted.connect(some_function)
        # self.accepted.connect(lambda: some_function(param))

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
        QSubWindow_set_your_working_directory.setWindowTitle(
            _translate("QSubWindow_set_your_working_directory", "Dialog"))
        self.label_5.setText(_translate("QSubWindow_set_your_working_directory", "Select your Working Directory"))
        self.pushButton_3.setToolTip(_translate("QSubWindow_set_your_working_directory",
                                                "<html><head/><body><p>Browse to Working Directory</p></body></html>"))
        self.pushButton_3.setText(_translate("QSubWindow_set_your_working_directory", "Browse"))
        self.buttonBox_2.setToolTip(_translate("QSubWindow_set_your_working_directory",
                                               "<html><head/><body><p>Press Ok to set your Working Directory</p><p>Press Cancel to Quit Dialog </p></body></html>"))

    def create_QSubWindow_set_your_working_directory(self):
        """
        This is the Method to Open the QSubWindow from the QMainWindow. This has to called from there.
        :return:
        """
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

