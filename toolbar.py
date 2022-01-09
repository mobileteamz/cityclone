from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
from tiles import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(20, 20, 150, 800)
        self.selected_option = None
        layout = QGridLayout()
        self.setLayout(layout)

        # Create pyqt toolbar
        for i in range(3):
            toolBar = QToolBar()
            layout.addWidget(toolBar)

            icon = QIcon("button_road.png")
            button_road = QPushButton()
            button_road.setAutoFillBackground(True)
            button_road.setStyleSheet("background-color: white")
            button_road.setIcon(icon)
            button_road.clicked.connect(self.didPressButtonRoad)
            toolBar.addWidget(button_road)

            icon = QIcon("button_power_plant.png")
            button_power_plant = QPushButton()
            button_power_plant.setAutoFillBackground(True)
            button_power_plant.setStyleSheet("background-color: white")
            button_power_plant.setIcon(icon)
            button_power_plant.clicked.connect(self.didPressButtonPowerPlant)
            toolBar.addWidget(button_power_plant)

            icon = QIcon("police.png")
            button_power_plant = QPushButton()
            button_power_plant.setAutoFillBackground(True)
            button_power_plant.setStyleSheet("background-color: white")
            button_power_plant.setIcon(icon)
            button_power_plant.clicked.connect(self.didPressButtonPolice)
            toolBar.addWidget(button_power_plant)


    def didPressButtonRoad(self):
        self.selected_option = TILE_STREET

    def didPressButtonPowerPlant(self):
        self.selected_option = TILE_POWER_PLANT

    def didPressButtonPolice(self):
        self.selected_option = TILE_POLICE_DEPARTMENT