from PyQt5.QtWidgets import *

from UI.encryptionOrDecryption import EncryptionOrDecryptionDialog


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout();
        self.label = QLabel("Visual Simulation of CAST-128 algorithm")
        self.startButton = QPushButton("Start")

        layout.addWidget(self.label)
        layout.addWidget(self.startButton)
        self.setLayout(layout)

        self.startButton.clicked.connect(self.openEncryptionOrDecryptionDialog)

    def openEncryptionOrDecryptionDialog(self):
        self.hide()
        encryptionOrDecryptionDialog = EncryptionOrDecryptionDialog()
        encryptionOrDecryptionDialog.exec_()
