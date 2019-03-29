# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from auxilliary.environment import Environment
from gammaGUIv2.gui_windows.QSubWindow_set_your_working_directory import Ui_QSubWindow_set_your_working_directory
from gammaGUIv2.gui_windows.QSubWindow_data_extraction import Ui_QSubWindow_data_extraction
from gammaGUIv2.gui_windows.QSubWindow_S1_TOPS import Ui_QSubWindow_S1_TOPS
from gammaGUIv2.gui_windows.QSubWindow_S1_GRD import Ui_QSubWindow_S1_GRD

class Ui_MainWindow(object):
    """
    This is the QMainWindow Class. This class contains the hole Layout of the Main Window.
    This file is executed in the app_gammaGUI.py
    Here you can link the MainWindow with all QSubWindows via triggered.connect()
    """
    def setupUi(self, MainWindow):
        """
        This the the Setup Method for the UI
        :param MainWindow:
        :return:
        """
        ###
        # Set up for Main Window
        ###
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(720, 536)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)

        ###
        # Set the Backgroundimage
        ###
        self.oImage = QtGui.QImage(Environment.backgroundImage)
        self.sImage = self.oImage.scaled(QtCore.QSize(720, 536))
        self.palette = QtGui.QPalette()
        self.palette.setBrush(10, QtGui.QBrush(self.sImage))
        MainWindow.setPalette(self.palette)

        ###
        # Create all Objects in MainWindow
        ###
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 720, 21))
        self.menubar.setObjectName("menubar")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        self.menuGeneral_Data_Import = QtWidgets.QMenu(self.menuImport)
        self.menuGeneral_Data_Import.setObjectName("menuGeneral_Data_Import")
        self.menuSentinel1 = QtWidgets.QMenu(self.menuGeneral_Data_Import)
        self.menuSentinel1.setObjectName("menuSentinel1")
        self.menuAUX = QtWidgets.QMenu(self.menubar)
        self.menuAUX.setObjectName("menuAUX")
        self.menuGAMMA = QtWidgets.QMenu(self.menubar)
        self.menuGAMMA.setObjectName("menuGAMMA")
        self.menuISP_2 = QtWidgets.QMenu(self.menuGAMMA)
        self.menuISP_2.setObjectName("menuISP_2")
        self.menuGEO = QtWidgets.QMenu(self.menuGAMMA)
        self.menuGEO.setObjectName("menuGEO")
        self.menuLAT_2 = QtWidgets.QMenu(self.menuGAMMA)
        self.menuLAT_2.setObjectName("menuLAT_2")
        self.menuDISP_2 = QtWidgets.QMenu(self.menuGAMMA)
        self.menuDISP_2.setObjectName("menuDISP_2")
        self.menuSNAP = QtWidgets.QMenu(self.menubar)
        self.menuSNAP.setObjectName("menuSNAP")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ###
        # Action Data -> Make Subfolder in Menubar
        ###
        self.actionData_Extraction = QtWidgets.QAction(MainWindow)
        self.actionData_Extraction.setCheckable(False)
        self.actionData_Extraction.setObjectName("actionData_Extraction")
        self.actionSLC_Multilooking = QtWidgets.QAction(MainWindow)
        self.actionSLC_Multilooking.setObjectName("actionSLC_Multilooking")
        self.actionMultilooking = QtWidgets.QAction(MainWindow)
        self.actionMultilooking.setObjectName("actionMultilooking")
        self.actionInterferogram_Generation = QtWidgets.QAction(MainWindow)
        self.actionInterferogram_Generation.setObjectName("actionInterferogram_Generation")
        self.actionBaseline_Estimation = QtWidgets.QAction(MainWindow)
        self.actionBaseline_Estimation.setObjectName("actionBaseline_Estimation")
        self.actionInterferogram_Flattening = QtWidgets.QAction(MainWindow)
        self.actionInterferogram_Flattening.setObjectName("actionInterferogram_Flattening")
        self.actionCoherence_Estimation = QtWidgets.QAction(MainWindow)
        self.actionCoherence_Estimation.setObjectName("actionCoherence_Estimation")
        self.actionSRTM_preperation = QtWidgets.QAction(MainWindow)
        self.actionSRTM_preperation.setObjectName("actionSRTM_preperation")
        self.actionDEM_preperation = QtWidgets.QAction(MainWindow)
        self.actionDEM_preperation.setObjectName("actionDEM_preperation")
        self.actionGeocoding = QtWidgets.QAction(MainWindow)
        self.actionGeocoding.setObjectName("actionGeocoding")
        self.actionPolarimetry = QtWidgets.QAction(MainWindow)
        self.actionPolarimetry.setObjectName("actionPolarimetry")
        self.actionFiltering = QtWidgets.QAction(MainWindow)
        self.actionFiltering.setObjectName("actionFiltering")
        self.actionMultilook = QtWidgets.QAction(MainWindow)
        self.actionMultilook.setObjectName("actionMultilook")
        self.actionSingle_Look_Complex = QtWidgets.QAction(MainWindow)
        self.actionSingle_Look_Complex.setObjectName("actionSingle_Look_Complex")
        self.actionCoherence = QtWidgets.QAction(MainWindow)
        self.actionCoherence.setObjectName("actionCoherence")
        self.actionInterferogram = QtWidgets.QAction(MainWindow)
        self.actionInterferogram.setObjectName("actionInterferogram")
        self.actionPhase = QtWidgets.QAction(MainWindow)
        self.actionPhase.setObjectName("actionPhase")
        self.actionHeight_Images = QtWidgets.QAction(MainWindow)
        self.actionHeight_Images.setObjectName("actionHeight_Images")
        self.actionExport_Import = QtWidgets.QAction(MainWindow)
        self.actionExport_Import.setObjectName("actionExport_Import")
        self.actionLayer_Stacking = QtWidgets.QAction(MainWindow)
        self.actionLayer_Stacking.setObjectName("actionLayer_Stacking")
        self.actionSentinel_1_TOPS = QtWidgets.QAction(MainWindow)
        self.actionSentinel_1_TOPS.setObjectName("actionSentinel_1_TOPS")
        self.actionERS = QtWidgets.QAction(MainWindow)
        self.actionERS.setObjectName("actionERS")
        self.actionTDX = QtWidgets.QAction(MainWindow)
        self.actionTDX.setObjectName("actionTDX")
        self.actionTSX = QtWidgets.QAction(MainWindow)
        self.actionTSX.setObjectName("actionTSX")
        self.actionSet_Working_Dir = QtWidgets.QAction(MainWindow)
        self.actionSet_Working_Dir.setObjectName("actionSet_Working_Dir")
        self.actionCSK = QtWidgets.QAction(MainWindow)
        self.actionCSK.setObjectName("actionCSK")
        self.actionRS = QtWidgets.QAction(MainWindow)
        self.actionRS.setObjectName("actionRS")
        self.actionRS2 = QtWidgets.QAction(MainWindow)
        self.actionRS2.setObjectName("actionRS2")
        self.actionPSR2 = QtWidgets.QAction(MainWindow)
        self.actionPSR2.setObjectName("actionPSR2")
        self.actionSentinel2 = QtWidgets.QAction(MainWindow)
        self.actionSentinel2.setObjectName("actionSentinel2")
        self.actionLandsat7 = QtWidgets.QAction(MainWindow)
        self.actionLandsat7.setObjectName("actionLandsat7")
        self.actionLandsat8 = QtWidgets.QAction(MainWindow)
        self.actionLandsat8.setObjectName("actionLandsat8")
        self.actionSLC_Multilooking_2 = QtWidgets.QAction(MainWindow)
        self.actionSLC_Multilooking_2.setObjectName("actionSLC_Multilooking_2")
        self.actionMultilooking_2 = QtWidgets.QAction(MainWindow)
        self.actionMultilooking_2.setObjectName("actionMultilooking_2")
        self.actionInterferogram_Generation_2 = QtWidgets.QAction(MainWindow)
        self.actionInterferogram_Generation_2.setObjectName("actionInterferogram_Generation_2")
        self.actionBaseline_Estimation_2 = QtWidgets.QAction(MainWindow)
        self.actionBaseline_Estimation_2.setObjectName("actionBaseline_Estimation_2")
        self.actionInterferogram_Flattening_2 = QtWidgets.QAction(MainWindow)
        self.actionInterferogram_Flattening_2.setObjectName("actionInterferogram_Flattening_2")
        self.actionCoherence_Estimation_2 = QtWidgets.QAction(MainWindow)
        self.actionCoherence_Estimation_2.setObjectName("actionCoherence_Estimation_2")
        self.actionSRTM_preperation_2 = QtWidgets.QAction(MainWindow)
        self.actionSRTM_preperation_2.setObjectName("actionSRTM_preperation_2")
        self.actionDEM_preperation_2 = QtWidgets.QAction(MainWindow)
        self.actionDEM_preperation_2.setObjectName("actionDEM_preperation_2")
        self.actionGeocoding_2 = QtWidgets.QAction(MainWindow)
        self.actionGeocoding_2.setObjectName("actionGeocoding_2")
        self.actionPolarimetry_2 = QtWidgets.QAction(MainWindow)
        self.actionPolarimetry_2.setObjectName("actionPolarimetry_2")
        self.actionFiltering_2 = QtWidgets.QAction(MainWindow)
        self.actionFiltering_2.setObjectName("actionFiltering_2")
        self.actionMultilook_2 = QtWidgets.QAction(MainWindow)
        self.actionMultilook_2.setObjectName("actionMultilook_2")
        self.actionSingle_Look_Complex_2 = QtWidgets.QAction(MainWindow)
        self.actionSingle_Look_Complex_2.setObjectName("actionSingle_Look_Complex_2")
        self.actionCoherence_2 = QtWidgets.QAction(MainWindow)
        self.actionCoherence_2.setObjectName("actionCoherence_2")
        self.actionInterferogram_2 = QtWidgets.QAction(MainWindow)
        self.actionInterferogram_2.setObjectName("actionInterferogram_2")
        self.actionPhase_2 = QtWidgets.QAction(MainWindow)
        self.actionPhase_2.setObjectName("actionPhase_2")
        self.actionHeight_Images_2 = QtWidgets.QAction(MainWindow)
        self.actionHeight_Images_2.setObjectName("actionHeight_Images_2")
        self.actionPlotting = QtWidgets.QAction(MainWindow)
        self.actionPlotting.setObjectName("actionPlotting")
        self.actionS1_TOPS = QtWidgets.QAction(MainWindow)
        self.actionS1_TOPS.setObjectName("actionS1_TOPS")
        self.actionS1_GRD = QtWidgets.QAction(MainWindow)
        self.actionS1_GRD.setObjectName("actionS1_GRD")


        """
        1. Step of Implementation
        -> Create a connection to QSubWindows
        -> use self.action{}.triggered.connect(Ui_QSubWindow{}.create_QSubWindow_{})
        
        Example:        
        self.menuImport.addAction(self.actionSet_Working_Dir)
        self.actionSet_Working_Dir.triggered.connect(Ui_QSubWindow_set_your_working_directory.create_QSubWindow_set_your_working_directory)
        
        Workflow: 
            - Link the QSubWindow to QMainWindow Entries (Menubar)
                - Therefore : 
                                -   Import from gammaGUIv2.gui_windows the wanted Ui_QSubWindows_{}
                                    e.g  from gammaGUIv2.gui_windows.QSubWindow_set_your_working_directory import Ui_QSubWindow_set_your_working_directory
                                    
                                -   Find Place in Script were the Entry is called: 
                                    e.g. self.menuImport.addAction(self.actionSet_Working_Dir)
                                         self.actionSet_Working_Dir.triggered.connect(Ui_QSubWindow_set_your_working_directory.create_QSubWindow_set_your_working_directory)
                                         
            - After that you Can modify the SubWindows (Buttons etc.) -> Button clicked -> def do_something
                - Therefore:
                                -   Open QSubWindow_{}.py
                                -   Set your Imports
                                    e.g. from auxilliary.environment import Environment
                                        from gammaGUIv2.gui_windows.QBrowseDialoge import BrowseDialoge
                                        
                                -   Find Place in Script were the Buttons are Created to add Functionality to them:
                                    e.g. self.pushButton_3.setObjectName("pushButton_3")
                                         self.pushButton_3.clicked.connect(BrowseDialoge.browse_function)
                                         self.pushButton_4.clicked.connect(BrowseDialogeOdir.browse_function)
                                         self.lineEdit_3.setPlaceholderText(Environment.wdir)
                                         self.buttonBox_2.accepted.connect(ZippedFiles.unzip_files)
                                         
            - HAVE FUN WITH CODING
                - Therefore:
                                - Write your own Stuff, and learn python while your creating a GUI
                                - If you are at the End of the Script open the QSubWindow_{}.py   
        """
        ###
        # Set Action to S1_TOPS
        ###
        self.menuSentinel1.addAction(self.actionS1_TOPS)
        self.actionS1_TOPS.triggered.connect(Ui_QSubWindow_S1_TOPS.create_Ui_QSubWindow_S1_TOPS)

        ###
        # Set Action to S1_GRD
        ###
        self.menuSentinel1.addAction(self.actionS1_GRD)
        self.actionS1_GRD.triggered.connect(Ui_QSubWindow_S1_GRD.create_Ui_QSubWindow_S1_GRD)

        self.menuGeneral_Data_Import.addAction(self.menuSentinel1.menuAction())
        self.menuGeneral_Data_Import.addAction(self.actionERS)
        self.menuGeneral_Data_Import.addAction(self.actionTDX)
        self.menuGeneral_Data_Import.addAction(self.actionTSX)
        self.menuGeneral_Data_Import.addAction(self.actionCSK)
        self.menuGeneral_Data_Import.addAction(self.actionRS)
        self.menuGeneral_Data_Import.addAction(self.actionRS2)
        self.menuGeneral_Data_Import.addAction(self.actionPSR2)
        self.menuGeneral_Data_Import.addSeparator()
        self.menuGeneral_Data_Import.addAction(self.actionSentinel2)
        self.menuGeneral_Data_Import.addAction(self.actionLandsat7)
        self.menuGeneral_Data_Import.addAction(self.actionLandsat8)

        ###
        # Set Action to Working Directory
        ###
        self.menuImport.addAction(self.actionSet_Working_Dir)
        self.actionSet_Working_Dir.triggered.connect(Ui_QSubWindow_set_your_working_directory.create_QSubWindow_set_your_working_directory)

        ###
        # Set Action to Data_Extraction
        ###
        self.menuImport.addAction(self.actionData_Extraction)
        self.actionData_Extraction.triggered.connect(Ui_QSubWindow_data_extraction.create_Ui_QSubWindow_data_extraction)


        self.menuImport.addSeparator()
        self.menuImport.addAction(self.menuGeneral_Data_Import.menuAction())
        self.menuAUX.addAction(self.actionExport_Import)
        self.menuAUX.addAction(self.actionLayer_Stacking)
        self.menuAUX.addSeparator()
        self.menuAUX.addAction(self.actionPlotting)
        self.menuISP_2.addAction(self.actionSLC_Multilooking_2)
        self.menuISP_2.addAction(self.actionMultilooking_2)
        self.menuISP_2.addAction(self.actionInterferogram_Generation_2)
        self.menuISP_2.addAction(self.actionBaseline_Estimation_2)
        self.menuISP_2.addAction(self.actionInterferogram_Flattening_2)
        self.menuISP_2.addAction(self.actionCoherence_Estimation_2)
        self.menuGEO.addAction(self.actionSRTM_preperation_2)
        self.menuGEO.addAction(self.actionDEM_preperation_2)
        self.menuGEO.addAction(self.actionGeocoding_2)
        self.menuLAT_2.addAction(self.actionPolarimetry_2)
        self.menuLAT_2.addAction(self.actionFiltering_2)
        self.menuDISP_2.addAction(self.actionMultilook_2)
        self.menuDISP_2.addAction(self.actionSingle_Look_Complex_2)
        self.menuDISP_2.addAction(self.actionCoherence_2)
        self.menuDISP_2.addAction(self.actionInterferogram_2)
        self.menuDISP_2.addAction(self.actionPhase_2)
        self.menuDISP_2.addAction(self.actionHeight_Images_2)
        self.menuGAMMA.addAction(self.menuISP_2.menuAction())
        self.menuGAMMA.addAction(self.menuGEO.menuAction())
        self.menuGAMMA.addAction(self.menuLAT_2.menuAction())
        self.menuGAMMA.addAction(self.menuDISP_2.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuGAMMA.menuAction())
        self.menubar.addAction(self.menuSNAP.menuAction())
        self.menubar.addAction(self.menuAUX.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        """
        This is the Method to rename every Entry in the Window.
        If you want to Change Names DO IT HERE
        :param MainWindow:
        :return:
        """
        ###
        # "&ISP" -> Short Cut Alt+I -> Select tab by Keyboard
        ##
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gamma GUI v2"))
        self.menuImport.setTitle(_translate("MainWindow", "&Import"))
        self.menuGeneral_Data_Import.setTitle(_translate("MainWindow", "General Data Import"))
        self.menuSentinel1.setTitle(_translate("MainWindow", "Sentinel1"))
        self.menuAUX.setTitle(_translate("MainWindow", "&AUX"))
        self.menuGAMMA.setTitle(_translate("MainWindow", "&GAMMA"))
        self.menuISP_2.setTitle(_translate("MainWindow", "ISP"))
        self.menuGEO.setTitle(_translate("MainWindow", "GEO"))
        self.menuLAT_2.setTitle(_translate("MainWindow", "LAT"))
        self.menuDISP_2.setTitle(_translate("MainWindow", "DISP"))
        self.menuSNAP.setTitle(_translate("MainWindow", "&SNAP"))
        self.actionData_Extraction.setText(_translate("MainWindow", "Data Extraction"))
        self.actionSLC_Multilooking.setText(_translate("MainWindow", "SLC Multilooking"))
        self.actionMultilooking.setText(_translate("MainWindow", "Multilooking"))
        self.actionInterferogram_Generation.setText(_translate("MainWindow", "Interferogram Generation"))
        self.actionBaseline_Estimation.setText(_translate("MainWindow", "Baseline Estimation"))
        self.actionInterferogram_Flattening.setText(_translate("MainWindow", "Interferogram Flattening"))
        self.actionCoherence_Estimation.setText(_translate("MainWindow", "Coherence Estimation"))
        self.actionSRTM_preperation.setText(_translate("MainWindow", "SRTM preperation"))
        self.actionDEM_preperation.setText(_translate("MainWindow", "DEM preperation"))
        self.actionGeocoding.setText(_translate("MainWindow", "Geocoding"))
        self.actionPolarimetry.setText(_translate("MainWindow", "Polarimetry"))
        self.actionFiltering.setText(_translate("MainWindow", "Filtering"))
        self.actionMultilook.setText(_translate("MainWindow", "Multilook"))
        self.actionSingle_Look_Complex.setText(_translate("MainWindow", "Single Look Complex"))
        self.actionCoherence.setText(_translate("MainWindow", "Coherence"))
        self.actionInterferogram.setText(_translate("MainWindow", "Interferogram"))
        self.actionPhase.setText(_translate("MainWindow", "Phase"))
        self.actionHeight_Images.setText(_translate("MainWindow", "Height Images"))
        self.actionExport_Import.setText(_translate("MainWindow", "Export/Import"))
        self.actionLayer_Stacking.setText(_translate("MainWindow", "Layer Stacking"))
        self.actionSentinel_1_TOPS.setText(_translate("MainWindow", "Sentinel 1 TOPS"))
        self.actionERS.setText(_translate("MainWindow", "ERS"))
        self.actionTDX.setText(_translate("MainWindow", "TDX"))
        self.actionTSX.setText(_translate("MainWindow", "TSX"))
        self.actionSet_Working_Dir.setText(_translate("MainWindow", "Set Working Directory"))
        self.actionCSK.setText(_translate("MainWindow", "CSK"))
        self.actionRS.setText(_translate("MainWindow", "RS2"))
        self.actionRS2.setText(_translate("MainWindow", "PSR1"))
        self.actionPSR2.setText(_translate("MainWindow", "PSR2"))
        self.actionSentinel2.setText(_translate("MainWindow", "Sentinel2"))
        self.actionLandsat7.setText(_translate("MainWindow", "Landsat7"))
        self.actionLandsat8.setText(_translate("MainWindow", "Landsat8"))
        self.actionSLC_Multilooking_2.setText(_translate("MainWindow", "SLC Multilooking"))
        self.actionMultilooking_2.setText(_translate("MainWindow", "Multilooking"))
        self.actionInterferogram_Generation_2.setText(_translate("MainWindow", "Interferogram Generation"))
        self.actionBaseline_Estimation_2.setText(_translate("MainWindow", "Baseline Estimation"))
        self.actionInterferogram_Flattening_2.setText(_translate("MainWindow", "Interferogram Flattening"))
        self.actionCoherence_Estimation_2.setText(_translate("MainWindow", "Coherence Estimation"))
        self.actionSRTM_preperation_2.setText(_translate("MainWindow", "SRTM preperation"))
        self.actionDEM_preperation_2.setText(_translate("MainWindow", "DEM preperation"))
        self.actionGeocoding_2.setText(_translate("MainWindow", "Geocoding"))
        self.actionPolarimetry_2.setText(_translate("MainWindow", "Polarimetry"))
        self.actionFiltering_2.setText(_translate("MainWindow", "Filtering"))
        self.actionMultilook_2.setText(_translate("MainWindow", "Multilook"))
        self.actionSingle_Look_Complex_2.setText(_translate("MainWindow", "Single Look Complex"))
        self.actionCoherence_2.setText(_translate("MainWindow", "Coherence"))
        self.actionInterferogram_2.setText(_translate("MainWindow", "Interferogram"))
        self.actionPhase_2.setText(_translate("MainWindow", "Phase"))
        self.actionHeight_Images_2.setText(_translate("MainWindow", "Height Images"))
        self.actionPlotting.setText(_translate("MainWindow", "Plotting"))
        self.actionS1_TOPS.setText(_translate("MainWindow", "S1 TOPS"))
        self.actionS1_GRD.setText(_translate("MainWindow", "S1 GRD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

