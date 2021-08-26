from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *

from UI.algorithm import AlgorithmDialog
from UI.errorDialog import ErrorDialog
from core.keyGenerator import getKeySize, checkKeyFormat
from core.splitPlainOrCipherText import getPlainOrCipherText, checkPlainOrCipherText


class StartDecryptionDialog(QDialog):
    def __init__(self, encryptionOrDecryption):
        QDialog.__init__(self)
        self.encryptionOrDecryption = encryptionOrDecryption;
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        labelCipherText = QLabel("CIPHERTEXT")
        self.cipherTextInput = QLineEdit("238B4FE5847E44B2")
        labelKey = QLabel("KEY")
        self.keyInput = QLineEdit("0123456712345678234567893456789A")
        self.backButton = QPushButton("Back")
        self.nextButton = QPushButton("Next")
        layout.addWidget(labelCipherText, 0, 0)
        layout.addWidget(self.cipherTextInput, 0, 1)
        layout.addWidget(labelKey, 1, 0)
        layout.addWidget(self.keyInput, 1, 1)
        layout.addWidget(self.backButton, 2, 3)
        layout.addWidget(self.nextButton, 2, 4)

        self.setLayout(layout)

        self.nextButton.clicked.connect(self.openAlgorithm)
        self.backButton.clicked.connect(self.openEncryptionOrDecryption)

    def openAlgorithm(self):
        h_size = getKeySize(self.keyInput.text())
        h_size_cipherText = getPlainOrCipherText(self.cipherTextInput.text())
        isCipherTextValid = checkPlainOrCipherText(self.cipherTextInput.text())
        isKeyValid = checkKeyFormat(self.keyInput.text())
        if h_size < 40:
            errorDialog = ErrorDialog("Key size must be grater than 40 bits!")
            errorDialog.exec_()
        elif h_size % 8 != 0:
            errorDialog = ErrorDialog("Key size must be in 8-bit increments!")
            errorDialog.exec_()
        elif h_size > 128:
            errorDialog = ErrorDialog("Key size must be less than 128 bits!")
            errorDialog.exec_()
        elif h_size_cipherText != 64:
            errorDialog = ErrorDialog("Cipher text size must be 64 bits!")
            errorDialog.exec_()
        elif not isCipherTextValid:
            errorDialog = ErrorDialog("Cipher text must be in hexadecimal format!")
            errorDialog.exec_()
        elif not isKeyValid:
            errorDialog = ErrorDialog("Key must be in hexadecimal format!")
            errorDialog.exec_()
        else:
            self.hide()
            algorithm = AlgorithmDialog(self.cipherTextInput.text(), self.keyInput.text(), False)
            algorithm.exec_()

    def openEncryptionOrDecryption(self):
        self.hide()
        self.encryptionOrDecryption.exec_()
