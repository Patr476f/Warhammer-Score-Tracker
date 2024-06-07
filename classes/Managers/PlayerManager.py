from PySide6 import QtCore, QtWidgets, QtGui

class PlayerManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QVBoxLayout()
        label = QtWidgets.QLabel("Player manager")
        layout.addWidget(label)
        self.setLayout(layout)