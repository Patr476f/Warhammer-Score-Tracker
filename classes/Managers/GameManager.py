from classes.Managers.MissionDeckManager import MissionDeckManager
from classes.Managers.PlayerManager import PlayerManager

from PySide6 import QtCore, QtWidgets, QtGui


class GameManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Game manager")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout()
        central_widget.setLayout(layout)

        self.tab_widget = QtWidgets.QTabWidget()
        layout.addWidget(self.tab_widget)

        self.MissionManager = MissionDeckManager()
        self.PlayerManager = PlayerManager()

        self.tab_widget.addTab(self.MissionManager, "Mission deck")
        self.tab_widget.addTab(self.PlayerManager, "Player")