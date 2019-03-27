from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
import sys
from MyGui import Second


class MainWindow(QMainWindow):

    # Konstruktor
    def __init__(self):

        # uebernimmt alle Funktionen von internen QMainWindow
        # Gehört generell immer dazu
        super().__init__()

        # Hier: rufe die Methode initUI auf
        # Diese erstellt alle Elemente auf der QMain-Oberfläche
        self.initUI()


    def initUI(self):

        # Set up for Main Window
        self.setObjectName("MainWindow")

        # Hier Größe des Fensters einstellen [erst Weite, dann Höhe]
        self.resize(720, 536)

        ############################################
        # Beispiel Hintergund einfuegen
        ############################################

        # Set the Backgroundimage
        # Erstellt eine Instanz von QImage --> QImage(Pfad)
        # Kann mit self.background image zum Attribut von der Klasse MainWindow gemacht werden
        background_Image = QImage("picture.jpg")

        # Skaliere das Bild auf die Größe des MainWindows
        background_Image = background_Image.scaled(QSize(720, 536))

        # Erstelle QPalette wil QImage kein QWidget ist
        palette = QPalette()

        # Uebergebe der Palette das Bild
        # Nummer entpricht Layout--> Hier Windows
        palette.setBrush(10, QBrush(background_Image))

        # Rufe Funktion von QMainWindow(Oberklasse) auf um Palette neu zu setzen
        self.setPalette(palette)


        #############################################
        # Beispiel Menuskelett(Unterpunkte etc. #####
        #############################################

        # Erschaffe eine Instanz von menubar
        # .menubar ist ein Attribut von der Klasse QMainWindow also hier MainWindow
        menubar_MainWindow = self.menuBar()
        # Bestimme die Größe
        menubar_MainWindow.setGeometry(QRect(0, 0, 720, 21))

        # Fuege Menues hinzu
        Import_Menu = menubar_MainWindow.addMenu("Import")

        # TODO: Momentan Platzhalter fuer zukuenftige Untermenues/Aktionen
        GAMMA_Menu = menubar_MainWindow.addMenu("GAMMA")
        SNAP_Menu = menubar_MainWindow.addMenu("SNAP")
        AUX_Menu = menubar_MainWindow.addMenu("AUX")


        # Fuege solange Menues hinzu bis etwas passieren soll
        General_Import_Menu = Import_Menu.addMenu("General Data Import")

        # Fuege Untermenues hinzu
        S1_Menu = General_Import_Menu.addMenu("Sentinel 1")

        ############################################
        # Beispiel Aktionen ########################
        ############################################
        # Aktionen sind die Ende von Menues -->  # Beim Anklicken soll etwas passieren
        # Es werden hier QActions verwendet

        # Menue Import:
        Set_Work_Dir_Action = QAction("Select Working Directory", self)
        Data_Extraction_Action = QAction("Data Extraction", self)

        # TODO: Momentan Platzhalter fuer zukuenftige Aktionen

        #
        # Menue_Genereal_Data_Import
        ERS_Action = QAction("ERS", self)
        TDX_Action = QAction("TDX", self)
        CSK_Action = QAction("CSK", self)
        RS2_Action = QAction("RS2", self)
        PSR1_Action = QAction("PRS1", self)
        PSR2_Action = QAction("PRS2", self)
        Sentinel2_Action = QAction("Sentinel 2", self)
        Landsat7_Action = QAction("Landsat 7", self)
        Landsat8_Action = QAction("Landsat8", self)

        # Menue_Sentinel 1
        S1_TOPS_Action = QAction("S1 TOPS", self)
        S1_GRD_Action = QAction("S1 GRD", self)

        # Alle Menues und alle Aktionen existieren jetzt
        # Nun muessen Aktionen und Menues verbunden werden

        # Import Level
        Import_Menu.addAction(Set_Work_Dir_Action)
        Import_Menu.addAction(Data_Extraction_Action)

        # General Data Level
        General_Import_Menu.addAction(ERS_Action)
        General_Import_Menu.addAction(TDX_Action)
        General_Import_Menu.addAction(CSK_Action)
        General_Import_Menu.addAction(RS2_Action)
        General_Import_Menu.addAction(PSR1_Action)
        General_Import_Menu.addAction(PSR2_Action)
        General_Import_Menu.addAction(Sentinel2_Action)
        General_Import_Menu.addAction(Landsat7_Action)
        General_Import_Menu.addAction(Landsat8_Action)

        # Sentinel 1 Level
        S1_Menu.addAction(S1_TOPS_Action)
        S1_Menu.addAction(S1_GRD_Action)

        # Momentan sind Aktionen und Menues verbunden
        # Aber die Aktionen sind noch leer bzw. Es gibt kein Signal-Input, was passieren soll
        # Hier wird triggered.connect(Methode, Funktion) verwendet

        # Ruft Methode (Klassenfunktion) Open_Set_Work_Dir_Window  auf
        Set_Work_Dir_Action.triggered.connect(self.Open_Set_Work_Dir_Window)

        # Rufe Methode Open_Data_Extraction_Window auf
        Data_Extraction_Action.triggered.connect(self.Open_Data_Extraction_Window)

        # Rufe Methode Open_Data_Extraction_Window auf
        S1_TOPS_Action.triggered.connect(self.Open_S1_TOPS_Window)

    # Jede Aktion erhält ein Fenster!!
    # So werden Funktionen die einer Klasse angehören geschrieben = Methode
    # Ruft eines neues Fenster auf (Hier: Working Directory Fenster)
    def Open_Set_Work_Dir_Window(self):
        # Erstellt eine Instanz der Working Directory Fenster
        self.test = Second()

        # Zeigt das Fenster
        self.test.show()

    # Ruft eines neues Fenster auf (Hier: Open_Data_Extraction_Window)
    def Open_Data_Extraction_Window(self):
        self.test = Second()
        self.test.show()

    # Ruft eines neues Fenster auf (Hier: Open_Data_Extraction_Window)
    def Open_S1_TOPS_Window(self):
        self.test = Second()
        self.test.show()

def main():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()