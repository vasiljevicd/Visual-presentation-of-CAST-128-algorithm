from PyQt5.QtWidgets import *

from UI.encryptionOrDecryption import EncryptionOrDecryptionDialog


class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Visual Presentation of CAST-128 algorithm")
        layout = QVBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QHBoxLayout()
        layoutMain = QVBoxLayout()
        self.startButton = QPushButton("Start")
        self.description = QLabel("Visual Presentation of CAST-128 algorithm is a software"  +"\n"
                                  "system which was developed as a part of bachelor thesis at " + "\n"
                                  "School of Electrical Engineering, University of Belgrade. "
                                  "\n"
                                  "\n"
                                  "\n"
                                  "\n"
                                  "\n"
                                  "\n"
                                  "\n"
                                  "\n"
                                  "\n")
        self.author = QLabel("Author: Danka Vasiljević")
        self.mentor = QLabel("Mentor: dr Žarko Stanisavljević")
        self.date = QLabel("Beograd, septembar 2021")

        layout.addWidget(self.description)

        layout1.addWidget(self.startButton)

        layout2.addWidget(self.author)
        layout2.addWidget(self.mentor)
        layout2.addWidget(self.date)

        layout3.addLayout(layout2)
        layout3.addLayout(layout1)

        layoutMain.addLayout(layout)
        layoutMain.addLayout(layout3)

        self.setLayout(layoutMain)

        self.startButton.clicked.connect(self.openEncryptionOrDecryptionDialog)

    def openEncryptionOrDecryptionDialog(self):
        self.hide()
        encryptionOrDecryptionDialog = EncryptionOrDecryptionDialog()
        encryptionOrDecryptionDialog.exec_()
