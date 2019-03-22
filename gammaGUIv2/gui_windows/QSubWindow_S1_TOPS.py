# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\gammaGUIv2\gammaGUIv2\Qt_Export\QSubWindow_S1_TOPS.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from gammaGUIv2.gui_windows.QBrowseDialoge import *
#from gamma.gamma_modules.S1_TOPS import S1TOPS
from gamma.gamma_modules.par_S1_tops import ParS1Tops

class Ui_QSubWindow_S1_TOPS(object):
    """
    TODO COMMENT AND MAKE IT PRETTY AND add ALL Functionality (only browse and ok are Working)
    """
    def setupUi(self, QSubWindow_S1_TOPS):

        QSubWindow_S1_TOPS.setObjectName("QSubWindow_S1_TOPS")
        QSubWindow_S1_TOPS.resize(774, 255)

        self.verticalLayout = QtWidgets.QVBoxLayout(QSubWindow_S1_TOPS)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalWidget_8 = QtWidgets.QWidget(QSubWindow_S1_TOPS)
        self.horizontalWidget_8.setObjectName("horizontalWidget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalWidget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)

        self.checkBox_3 = QtWidgets.QCheckBox(self.horizontalWidget_8)
        self.checkBox_3.setObjectName("checkBox_3")

        self.horizontalLayout_8.addWidget(self.checkBox_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalWidget = QtWidgets.QWidget(self.horizontalWidget_8)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalWidget)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_5.addWidget(self.radioButton_6)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalWidget)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_5.addWidget(self.radioButton_5)
        self.horizontalLayout_8.addWidget(self.verticalWidget)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)

        self.checkBox_4 = QtWidgets.QCheckBox(self.horizontalWidget_8)
        self.checkBox_4.setObjectName("checkBox_4")

        self.horizontalLayout_8.addWidget(self.checkBox_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)

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
        self.verticalWidget_5 = QtWidgets.QWidget(QSubWindow_S1_TOPS)
        self.verticalWidget_5.setObjectName("verticalWidget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalWidget_9 = QtWidgets.QWidget(self.verticalWidget_5)
        self.horizontalWidget_9.setObjectName("horizontalWidget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalWidget_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)

        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalWidget_9)
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.horizontalLayout_9.addWidget(self.lineEdit_3)

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

        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalWidget_10)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_10.addWidget(self.lineEdit_4)

        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalWidget_10)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(BrowseDialogeOdir.browse_function)
        self.horizontalLayout_10.addWidget(self.pushButton_4)

        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem11)
        self.verticalLayout_4.addWidget(self.horizontalWidget_10)
        self.verticalLayout_7.addWidget(self.verticalWidget_5)
        self.horizontalWidget_14 = QtWidgets.QWidget(QSubWindow_S1_TOPS)
        self.horizontalWidget_14.setObjectName("horizontalWidget_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.horizontalWidget_14)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem12)

        self.progressBar_2 = QtWidgets.QProgressBar(self.horizontalWidget_14)
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.horizontalLayout_14.addWidget(self.progressBar_2)

        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.horizontalWidget_14)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.buttonBox_2.accepted.connect(ParS1Tops.run_par_S1_tops)

        self.horizontalLayout_14.addWidget(self.buttonBox_2)

        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem13)
        self.verticalLayout_7.addWidget(self.horizontalWidget_14)
        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.retranslateUi(QSubWindow_S1_TOPS)
        QtCore.QMetaObject.connectSlotsByName(QSubWindow_S1_TOPS)

    def retranslateUi(self, QSubWindow_S1_TOPS):
        _translate = QtCore.QCoreApplication.translate
        QSubWindow_S1_TOPS.setWindowTitle(_translate("QSubWindow_S1_TOPS", "Dialog"))
        self.checkBox_3.setToolTip(_translate("QSubWindow_S1_TOPS", "<html><head/><body><p>Selects all Files in the Import Folder</p></body></html>"))
        self.checkBox_3.setText(_translate("QSubWindow_S1_TOPS", "Select all Files"))
        self.radioButton_6.setToolTip(_translate("QSubWindow_S1_TOPS", "<html><head/><body><p>Select *.rar Data</p></body></html>"))
        self.radioButton_6.setText(_translate("QSubWindow_S1_TOPS", "deramp (S1 SLC onyl)"))
        self.radioButton_5.setToolTip(_translate("QSubWindow_S1_TOPS", "<html><head/><body><p>Select *.zip Data</p></body></html>"))
        self.radioButton_5.setText(_translate("QSubWindow_S1_TOPS", "mosaicing (S1 SLC only)"))
        self.checkBox_4.setToolTip(_translate("QSubWindow_S1_TOPS", "<html><head/><body><p>Check to Select Start and End Date of File Import</p></body></html>"))
        self.checkBox_4.setText(_translate("QSubWindow_S1_TOPS", "Select Files (Period of time)"))
        self.dateEdit_3.setToolTip(_translate("QSubWindow_S1_TOPS", "<html><head/><body><p>Select Start Date</p></body></html>"))
        self.label_5.setText(_translate("QSubWindow_S1_TOPS", "Start Date"))
        self.dateEdit_4.setToolTip(_translate("QSubWindow_S1_TOPS", "<html><head/><body><p>Select End Date</p></body></html>"))
        self.label_6.setText(_translate("QSubWindow_S1_TOPS", "End Date"))
        self.pushButton_3.setToolTip(_translate("QSubWindow_S1_TOPS", "<html><head/><body><p>Browse to Import Folder</p></body></html>"))
        self.pushButton_3.setText(_translate("QSubWindow_S1_TOPS", "Browse"))
        self.pushButton_4.setToolTip(_translate("QSubWindow_S1_TOPS", "<html><head/><body><p>Browse to Output Folder</p></body></html>"))
        self.pushButton_4.setText(_translate("QSubWindow_S1_TOPS", "Browse"))
        self.buttonBox_2.setToolTip(_translate("QSubWindow_S1_TOPS", "<html><head/><body><p>Press Ok to Start Extraction</p><p>Press Cancel to Quit Dialog</p></body></html>"))

    def create_Ui_QSubWindow_S1_TOPS(self):
        QSubWindow_S1_TOPS = QtWidgets.QDialog()
        ui = Ui_QSubWindow_S1_TOPS()
        ui.setupUi(QSubWindow_S1_TOPS)
        QSubWindow_S1_TOPS.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QSubWindow_S1_TOPS = QtWidgets.QDialog()
    ui = Ui_QSubWindow_S1_TOPS()
    ui.setupUi(QSubWindow_S1_TOPS)
    QSubWindow_S1_TOPS.show()
    sys.exit(app.exec_())

