from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


# Main Window
from PyQt5.uic.properties import QtGui
from bitarray._util import ba2base
from bitarray.util import ba2int


class SboxWidget(QDialog):
    def __init__(self, Sbox, Iabcd, title):
        super().__init__()
        self.title = title

        self.setWindowTitle(self.title)
        self.sBox = Sbox
        self.Iabcd = Iabcd

        self.gridLayout = QGridLayout()

        for i in range(32):
            self.gridLayout.addWidget(QLabel(str(bin(i)[2:]).zfill(5)), i+1, 0)

        for j in range(8):
            self.gridLayout.addWidget(QLabel(str(bin(j)[2:]).zfill(3)), 0, j+1)

        for i in range(1, 33):
            for j in range(1, 9):
                self.gridLayout.addWidget(QLabel(str(self.sBox[i-1][j-1])), i, j)

        self.markOutput(self.Iabcd)

        self.setLayout(self.gridLayout)

    def markOutput(self, inputValue):
        row = ba2int(inputValue[0:5])+1
        column = ba2int(inputValue[5:8])+1
        output = self.gridLayout.itemAtPosition(row, column).widget()
        row = self.gridLayout.itemAtPosition(row, 0).widget()
        column = self.gridLayout.itemAtPosition(0, column).widget()
        myFont = QFont('Arial', 15)
        myFont.setBold(True)
        output.setFont(myFont)
        column.setFont(myFont)
        row.setFont(myFont)