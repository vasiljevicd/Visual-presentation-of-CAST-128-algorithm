from PyQt5.QtWidgets import *

from UI.algorithm import AlgorithmDialog
from UI.errorDialog import ErrorDialog
from core.keyGenerator import getKeySize, checkKeyFormat
from core.splitPlainOrCipherText import getPlainOrCipherText, checkPlainOrCipherText


class StartEncryptionDialog(QDialog):
    def __init__(self, encryptionOrDecryption):
        QDialog.__init__(self)
        self.encryptionOrDecryption = encryptionOrDecryption
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        labelPlainText = QLabel("PLAINTEXT")
        self.plainTextInput = QLineEdit()
        self.plainTextInput.setText("0123456789ABCDEF")
        labelKey = QLabel("KEY")
        self.keyInput = QLineEdit()
        self.keyInput.setText("0123456712345678234567893456789A")
        self.backButton = QPushButton("Back")
        self.nextButton = QPushButton("Next")
        layout.addWidget(labelPlainText, 0, 0)
        layout.addWidget(self.plainTextInput, 0, 1)
        layout.addWidget(labelKey, 1, 0)
        layout.addWidget(self.keyInput, 1, 1)
        layout.addWidget(self.backButton, 2, 3)
        layout.addWidget(self.nextButton, 2, 4)

        self.setLayout(layout)

        self.backButton.clicked.connect(self.openEncryptionOrDecryption)
        self.nextButton.clicked.connect(self.openAlgorithm)


    def openEncryptionOrDecryption(self):
        self.hide()
        self.encryptionOrDecryption.exec_()

    def openAlgorithm(self):
        h_size = getKeySize(self.keyInput.text())
        h_size_plainText = getPlainOrCipherText(self.plainTextInput.text())
        isPlainTextValid = checkPlainOrCipherText(self.plainTextInput.text())
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
        elif h_size_plainText != 64:
            errorDialog = ErrorDialog("Plain text size must be 64 bits!")
            errorDialog.exec_()
        elif not isPlainTextValid:
            errorDialog = ErrorDialog("Plain text must be in hexadecimal format!")
            errorDialog.exec_()
        elif not isKeyValid:
            errorDialog = ErrorDialog("Key must be in hexadecimal format!")
            errorDialog.exec_()
        else:
            self.hide()
            algorithm = AlgorithmDialog(self.plainTextInput.text(), self.keyInput.text(), True)
            algorithm.exec_()