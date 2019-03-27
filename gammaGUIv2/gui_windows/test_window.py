from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *
import sys

class Second(QWidget):
    def __init__(self):
        super().__init__()

        # Hier: rufe die Methode initUI auf
        # Diese erstellt alle Elemente auf der QMain-Oberfläche
        self.initUI()

    def initUI(self):
        # Set up for Main Window
        self.setObjectName("Test")

        # Hier Größe des Fensters einstellen [erst Weite, dann Höhe]
        self.resize(720, 536)