from PyQt5.QtWidgets import *
from bitarray._util import *

from UI.generatedKeysDialog import GeneratedKeysDialog
from UI.tabWidget import TabWidget
from core.keyGenerator import keyGenerator, keyHexToBinary
from core.rounds import roundsForAlgorithm, divideITo4Parts
from core.sboxes import calculatingSboxOutput
from core.splitPlainOrCipherText import splitPlainOrCipherText


class AlgorithmDialog(QDialog):
    def __init__(self, text, key, encryptionOrDecryption):
        QDialog.__init__(self)
        self.text = text
        self.key = key
        self.encryptionOrDecryption = encryptionOrDecryption
        keyBinary, self.numberOfRounds  = keyHexToBinary(self.key)
        self.Km = [None] * self.numberOfRounds
        self.Kr = [None] * self.numberOfRounds
        self.L = [None] * (self.numberOfRounds + 1)
        self.R = [None] * (self.numberOfRounds + 1)
        self.I = [None] * self.numberOfRounds
        self.f = [None] * self.numberOfRounds
        self.i = 0
        self.Km, self.Kr = keyGenerator(keyBinary)
        if not encryptionOrDecryption:
            self.L[self.numberOfRounds], self.R[self.numberOfRounds] = splitPlainOrCipherText(self.text)
        else:
            self.L[0], self.R[0] = splitPlainOrCipherText(self.text)
        self.L, self.R, self.Km, self.Kr, self.I, self.f = roundsForAlgorithm(self.L, self.R, self.Km, self.Kr,
                                                                              self.numberOfRounds, self.encryptionOrDecryption)

        if not encryptionOrDecryption:
            self.L.reverse()
            self.R.reverse()
            self.I.reverse()
            self.f.reverse()
            self.Km.reverse()
            self.Kr.reverse()

        self.initUI()
        self.generatedKeys.clicked.connect(self.openGeneratedKeys)
        self.nextRound.clicked.connect(lambda: self.tabWidget.nextRoundFunction(True, self.encryptionOrDecryption))
        self.previousRound.clicked.connect(lambda: self.tabWidget.nextRoundFunction(False, self.encryptionOrDecryption))
        self.newSimulation.clicked.connect(self.startNewSimulation)

    def initUI(self):
        layout = QVBoxLayout();
        tabWidgetLayout = QVBoxLayout()
        self.tabWidget = TabWidget(self.Km, self.Kr, self.L, self.R, self.I, self.f, self.numberOfRounds, self)
        tabWidgetLayout.addWidget(self.tabWidget)
        horizontalLayout = QHBoxLayout()
        self.roundCounter = QLabel("Round 1/ "+str(self.numberOfRounds))
        self.generatedKeys = QPushButton("Generated keys")
        self.previousRound = QPushButton("Previous round")
        self.disableButtonPreviousRound()
        self.nextRound = QPushButton("Next round")
        self.newSimulation = QPushButton("New simulation")
        horizontalLayout.addWidget(self.roundCounter)
        horizontalLayout.addWidget(self.generatedKeys)
        horizontalLayout.addWidget(self.previousRound)
        horizontalLayout.addWidget(self.nextRound)
        horizontalLayout.addWidget(self.newSimulation)

        layout.addLayout(tabWidgetLayout)
        layout.addLayout(horizontalLayout)
        self.setLayout(layout)

    def disableButton(self):
        self.nextRound.setDisabled(True)

    def setRoundNumber(self, i):
        self.roundCounter.setText("Round "+str(i+1)+"/ "+str(self.numberOfRounds))

    def startNewSimulation(self):
        self.close()

    def disableButtonPreviousRound(self):
        self.previousRound.setDisabled(True)

    def enableButtonPreviousRound(self):
        self.previousRound.setDisabled(False)

    def openGeneratedKeys(self):
        generatedKeys = GeneratedKeysDialog()