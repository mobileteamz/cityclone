from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys
from tiles import *

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(20, 20, 150, 250)
        self.selected_option = TILE_STREET
        layout = QGridLayout()
        self.setLayout(layout)

        # toolBar = QToolBar()
        # layout.addWidget(toolBar)


        # Create pyqt toolbar
        for i in range(6):
            icon = QIcon("./art/button_road.png")
            button_road = QPushButton()
            button_road.setAutoFillBackground(True)
            button_road.setStyleSheet("background-color: white")
            button_road.setIcon(icon)
            button_road.clicked.connect(self.didPressButtonRoad)
            layout.addWidget(button_road)

            icon = QIcon("./art/button_power_plant.png")
            button_power_plant = QPushButton()
            button_power_plant.setAutoFillBackground(True)
            button_power_plant.setStyleSheet("background-color: white")
            button_power_plant.setIcon(icon)
            button_power_plant.clicked.connect(self.didPressButtonPowerPlant)
            layout.addWidget(button_power_plant)

            icon = QIcon("./art/police.png")
            button_power_plant = QPushButton()
            button_power_plant.setAutoFillBackground(True)
            button_power_plant.setStyleSheet("background-color: white")
            button_power_plant.setIcon(icon)
            button_power_plant.clicked.connect(self.didPressButtonPolice)
            layout.addWidget(button_power_plant)


            # 
            icon = QIcon("./art/police.png")
            button_residential = QPushButton()
            button_residential.setAutoFillBackground(True)
            button_residential.setStyleSheet("background-color: white")
            button_residential.setIcon(icon)
            button_residential.clicked.connect(self.didPressButtonPolice)

            layout.addWidget(button_residential)


    def didPressButtonRoad(self):
        self.selected_option = TILE_STREET

    def didPressButtonPowerPlant(self):
        self.selected_option = TILE_POWER_PLANT

    def didPressButtonPolice(self):
        self.selected_option = TILE_POLICE_DEPARTMENT