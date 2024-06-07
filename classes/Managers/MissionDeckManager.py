from PySide6 import QtCore, QtWidgets, QtGui

class MissionDeckManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Mission deck manager")
        layout.addWidget(label)
        self.setLayout(layout)