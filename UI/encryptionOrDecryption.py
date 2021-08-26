from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *

from UI.startDecryption import StartDecryptionDialog
from UI.startEncryption import StartEncryptionDialog


class EncryptionOrDecryptionDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout();
        label = QLabel("Choose operation:")
        self.encryptionRB = QRadioButton("Encryption")
        self.encryptionRB.setChecked(True)
        self.decryptionRB = QRadioButton("Decryption")
        self.chooseButton = QPushButton("Next")
        self.chooseButton.clicked.connect(self.openStartSimulationPage)

        layout.addWidget(label)
        layout.addWidget(self.encryptionRB)
        layout.addWidget(self.decryptionRB)
        layout.addWidget(self.chooseButton)
        self.setLayout(layout)

    def openStartSimulationPage(self):
        #self.hide()
        if self.encryptionRB.isChecked() == True:
            startEncryption = StartEncryptionDialog(self)
            startEncryption.setFixedSize(QSize(600, 250))
            startEncryption.exec_()
        if self.decryptionRB.isChecked() == True:
            startDecryption = StartDecryptionDialog(self)
            startDecryption.setFixedSize(QSize(600, 250))
            startDecryption.exec_()


