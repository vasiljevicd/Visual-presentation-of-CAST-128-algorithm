from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from bitarray._util import *

from UI.sBoxWidget import SboxWidget
from core.keyGenerator import divideKeyTo8Parts
from core.rounds import divideITo4Parts
from core.sboxes import calculatingSboxOutput, sboxes


class TabWidget(QTabWidget):
    def __init__(self, Km, Kr, L, R, I, f, numberOfRounds, algorithmDialog):
        super(TabWidget, self).__init__()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.Km = Km
        self.Kr = Kr
        self.L = L
        self.R = R
        self.I = I
        self.f = f
        self.i = 0
        self.numberOfRounds = numberOfRounds
        self.algorithmDialog = algorithmDialog
        self.sBoxes = sboxes
        self.addTab(self.tab1, "Step 1")
        self.addTab(self.tab2, "Step 2")
        self.addTab(self.tab3, "Step 3")
        self.addTab(self.tab4, "Step 4")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()

        self.Sbox1.clicked.connect(lambda: self.openSBoxWidget(self.sBoxes[0], self.Iabcd[0], "Sbox1"))
        self.Sbox2.clicked.connect(lambda: self.openSBoxWidget(self.sBoxes[1], self.Iabcd[1], "Sbox2"))
        self.Sbox3.clicked.connect(lambda: self.openSBoxWidget(self.sBoxes[2], self.Iabcd[2], "Sbox3"))
        self.Sbox4.clicked.connect(lambda: self.openSBoxWidget(self.sBoxes[3], self.Iabcd[3], "Sbox4"))

    def nextRoundFunction(self, previousOrNext, encryptionOrDecryption):
        if previousOrNext:
            self.i = self.i + 1
            self.algorithmDialog.enableButtonPreviousRound()
        else:
            self.i = self.i - 1
            if self.i <= 0:
                self.algorithmDialog.disableButtonPreviousRound()

        if self.i == self.numberOfRounds-1:
            self.algorithmDialog.disableButton()
        self.setCurrentIndex(0)
        self.algorithmDialog.setRoundNumber(self.i)
        if self.i == 0 or self.i == 3 or self.i == 6 or self.i == 9 or self.i == 12 or self.i == 15:
            self.pixmaptab2 = QPixmap('UI/images/f1step2.png')
            self.pixmaptab2.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab2.setPixmap(self.pixmaptab2)
            self.pixmaptab3 = QPixmap('UI/images/f1step3.png')
            self.pixmaptab3.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab3.setPixmap(self.pixmaptab3)
            self.pixmaptab4 = QPixmap('UI/images/f1step4.png')
            self.pixmaptab4.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab4.setPixmap(self.pixmaptab4)
            self.Ivalue.setText(
                "  I = (Km" + str(self.i + 1) + " + R" + str(self.i + 1) + ") <<< Kr" + str(self.i + 1) +
                "\n"
                "\n " + self.formattingBits(self.Km[self.i]) + " "
                "\n"
                "\n                                 +                     "
                "\n"
                "\n " + self.formattingBits(self.R[self.i]) + "  "
                "\n"
                "\n                                <<<                    "
                "\n"
                "\n                              " + ba2base(2, self.Kr[self.i]) + " "
                "\n"
                "\n                                 =                     "
                "\n"
                "\n" + self.formattingBits(self.I[self.i]) + "")

            self.Fvalue.setText("F = ((S1[Ia] ^ S2[Ib]) - S3[Ic]) + S4[Id]"
                                 "\n"
                                 "\n" + self.formattingBits(calculatingSboxOutput(1, self.Iabcd[0])) +
                                 "\n"
                                 "\n                           ^"
                                 "\n"
                                 "\n" + self.formattingBits(calculatingSboxOutput(2, self.Iabcd[1])) +
                                 "\n"
                                 "\n                           -"
                                 "\n"
                                 "\n" + self.formattingBits(calculatingSboxOutput(3, self.Iabcd[2])) +
                                 "\n"
                                 "\n                           +"
                                 "\n"
                                 "\n" + self.formattingBits(calculatingSboxOutput(4, self.Iabcd[3])) +
                                 "\n"
                                 "\n                           ="
                                 "\n" + self.formattingBits(self.f[self.i]))

        # Rounds 2, 5, 8, 11, and 14 use f function Type 2.
        elif self.i == 1 or self.i == 4 or self.i == 7 or self.i == 10 or self.i == 13:
            self.pixmaptab2 = QPixmap('UI/images/f2step2.png')
            self.pixmaptab2.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab2.setPixmap(self.pixmaptab2)
            self.pixmaptab3 = QPixmap('UI/images/f2step3.png')
            self.pixmaptab3.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab3.setPixmap(self.pixmaptab3)
            self.pixmaptab4 = QPixmap('UI/images/f2step4.png')
            self.pixmaptab4.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab4.setPixmap(self.pixmaptab4)
            self.Ivalue.setText(
                "  I = (Km" + str(self.i + 1) + " ^ R" + str(self.i + 1) + ") <<< Kr" + str(self.i + 1) +
                "\n"
                "\n " + self.formattingBits(self.Km[self.i]) + " "
                                                               "\n"
                                                               "\n                                 ^                     "
                                                               "\n"
                                                               "\n " + self.formattingBits(self.R[self.i]) + "  "
                                                                                                             "\n"
                                                                                                             "\n                                <<<                    "
                                                                                                             "\n"
                                                                                                             "\n                              " + ba2base(
                    2, self.Kr[self.i]) + " "
                                          "\n"
                                          "\n                                 =                     "
                                          "\n"
                                          "\n" + self.formattingBits(self.I[self.i]) + "")

            self.Fvalue.setText("F = ((S1[Ia] - S2[Ib]) + S3[Ic]) ^ S4[Id]"
                                 "\n"
                                 "\n" + self.formattingBits(calculatingSboxOutput(1, self.Iabcd[0])) +
                                 "\n"
                                 "\n                           -"
                                 "\n"
                                 "\n" + self.formattingBits(calculatingSboxOutput(2, self.Iabcd[1])) +
                                 "\n"
                                 "\n                           +"
                                 "\n"
                                 "\n" + self.formattingBits(calculatingSboxOutput(3, self.Iabcd[2])) +
                                 "\n"
                                 "\n                           ^"
                                 "\n"
                                 "\n" + self.formattingBits(calculatingSboxOutput(4, self.Iabcd[3])) +
                                 "\n"
                                 "\n                           ="
                                 "\n"
                                 "\n" + self.formattingBits(self.f[self.i]))
            # Rounds 3, 6, 9, 12, and 15 use f function Type 3.
        elif self.i == 2 or self.i == 5 or self.i == 8 or self.i == 11 or self.i == 14:
            self.pixmaptab2 = QPixmap('UI/images/f3step2.png')
            self.pixmaptab2.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab2.setPixmap(self.pixmaptab2)
            self.pixmaptab3 = QPixmap('UI/images/f3step3.png')
            self.pixmaptab3.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab3.setPixmap(self.pixmaptab3)
            self.pixmaptab4 = QPixmap('UI/images/f3step4.png')
            self.pixmaptab4.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab4.setPixmap(self.pixmaptab4)
            self.Ivalue.setText(
                "  I = (Km" + str(self.i + 1) + " - R" + str(self.i + 1) + ") <<< Kr" + str(self.i + 1) +
                "\n"
                "\n " + self.formattingBits(self.Km[self.i]) + " "
                                                               "\n"
                                                               "\n                                 -                     "
                                                               "\n"
                                                               "\n " + self.formattingBits(self.R[self.i]) + "  "
                                                                                                             "\n"
                                                                                                             "\n                                <<<                    "
                                                                                                             "\n"
                                                                                                             "\n                              " + ba2base(
                    2, self.Kr[self.i]) + " "
                                          "\n"
                                          "\n                                 =                     "
                                          "\n"
                                          "\n" + self.formattingBits(self.I[self.i]) + "")

            self.Fvalue.setText("F = ((S1[Ia] + S2[Ib]) ^ S3[Ic]) - S4[Id]"
                                "\n"
                                "\n" + self.formattingBits(calculatingSboxOutput(1, self.Iabcd[0])) +
                                "\n"
                                "\n                           +"
                                "\n"
                                "\n" + self.formattingBits(calculatingSboxOutput(2, self.Iabcd[1])) +
                                "\n"
                                "\n                           ^"
                                "\n"
                                "\n" + self.formattingBits(calculatingSboxOutput(3, self.Iabcd[2])) +
                                "\n"
                                "\n                           -"
                                "\n"
                                "\n" + self.formattingBits(calculatingSboxOutput(4, self.Iabcd[3])) +
                                "\n"
                                "\n                           ="
                                "\n"
                                "\n" + self.formattingBits(self.f[self.i]))
        self.labelInputParams.setText("Input parameters for round " + str(self.i + 1))
        self.plainTextLeftSideLabel.setText(
            "Left side of data after round " + str(self.i) + " (L" + str(self.i + 1) + ")")
        self.plainTextRightSideLabel.setText(
            "Right side of data after round " + str(self.i) + " (R" + str(self.i + 1) + ")")
        self.plainTextLeftSide.setText(self.formattingBits(self.L[self.i]))
        self.plainTextRightSide.setText(self.formattingBits(self.R[self.i]))
        self.KmLabel.setText("Masking key (Km" + str(self.i + 1) + ")")
        self.KrLabel.setText("Rotation key (Kr" + str(self.i + 1) + ")")
        self.Km1.setText(self.formattingBits(self.Km[self.i]))
        self.Kr1.setText(ba2base(2, self.Kr[self.i]))

        # tab2
        # changing values for labels
        self.Iabcd = divideITo4Parts(self.I[self.i])
        self.IaValue.setText(ba2base(2, self.Iabcd[0]))
        self.IbValue.setText(ba2base(2, self.Iabcd[1]))
        self.IcValue.setText(ba2base(2, self.Iabcd[2]))
        self.IdValue.setText(ba2base(2, self.Iabcd[3]))
        self.Sbox1Value.setText(self.formattingBits(calculatingSboxOutput(1, self.Iabcd[0])))
        self.Sbox2Value.setText(self.formattingBits(calculatingSboxOutput(2, self.Iabcd[1])))
        self.Sbox3Value.setText(self.formattingBits(calculatingSboxOutput(3, self.Iabcd[2])))
        self.Sbox4Value.setText(self.formattingBits(calculatingSboxOutput(4, self.Iabcd[3])))
        # tab 3



        # tab 4
        if self.i == self.numberOfRounds-1 and encryptionOrDecryption:
            self.plainOrCipherlabel.setText("CIPHER TEXT = " + str(ba2hex(self.R[self.i + 1])).upper() + str(ba2hex(self.L[self.i + 1])).upper())
            self.Llabel.setText("")
            self.pixmaptab4 = QPixmap('')
            self.pixmaptab4.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab4.setPixmap(self.pixmaptab4)
        elif self.i == self.numberOfRounds-1 and not encryptionOrDecryption:
            self.plainOrCipherlabel.setText("PLAIN TEXT = " + str(ba2hex(self.R[self.i + 1])).upper() + str(ba2hex(self.L[self.i + 1])).upper())
            self.Llabel.setText("")
            self.pixmaptab4 = QPixmap('')
            self.pixmaptab4.scaled(32, 32, Qt.KeepAspectRatio)
            self.labeltab4.setPixmap(self.pixmaptab4)
        else:
            self.Llabel.setText(" L" + str(self.i + 2) + " = R" + str(self.i + 1) +
                                 "\n"
                                 "\nL" + str(self.i + 2) + " = " + self.formattingBits(self.R[self.i + 1]) +
                                 "\n"
                                 "\nR" + str(self.i + 2) + " = L" + str(self.i + 1) + " ^ F"
                                                                                     "\n"
                                                                                     "\n" + self.formattingBits(
                self.L[self.i]) +
                                 "\n"
                                 "\n                  ^"
                                 "\n"
                                 "\n" + self.formattingBits(self.f[self.i]) +
                                 "\n"
                                 "\n                  ="
                                 "\n"
                                 "\n" + self.formattingBits((self.L[self.i] ^ self.f[self.i])))

    def tab1UI(self):
        layout = QHBoxLayout()
        # tab1
        formLayout = QFormLayout()
        self.labelInputParams = QLabel("Input parameters for round " + str(self.i + 1))
        formLayout.addWidget(self.labelInputParams)
        self.Km1 = QLabel(self.formattingBits(self.Km[self.i]))
        self.Kr1 = QLabel(ba2base(2, self.Kr[self.i]))
        self.KmLabel = QLabel("Masking key (Km" + str(self.i + 1) + ")")
        self.KrLabel = QLabel("Rotation key (Kr" + str(self.i + 1) + ")")
        self.plainTextLeftSide = QLabel(self.formattingBits(self.L[self.i]))
        self.plainTextRightSide = QLabel(self.formattingBits(self.R[self.i]))
        self.plainTextLeftSideLabel = QLabel("Left side of plain text (L" + str(self.i + 1) + ")")
        self.plainTextRightSideLabel = QLabel("Right side of plain text (R" + str(self.i + 1) + ")")
        formLayout.addRow(self.plainTextLeftSideLabel, self.plainTextLeftSide)
        formLayout.addRow(self.plainTextRightSideLabel, self.plainTextRightSide)
        formLayout.addRow(self.KmLabel, self.Km1)
        formLayout.addRow(self.KrLabel, self.Kr1)

        pictureLayout = QVBoxLayout()
        self.labeltab1 = QLabel(self)
        self.pixmaptab1 = QPixmap('UI/images/CAST-128.png')
        self.pixmaptab1.scaled(32, 32, Qt.KeepAspectRatio)
        self.labeltab1.setPixmap(self.pixmaptab1)
        pictureLayout.addWidget(self.labeltab1)

        self.setTabText(0, "Step 1")
        layout.addLayout(formLayout)
        layout.addLayout(pictureLayout)
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QHBoxLayout()
        layoutLabels = QVBoxLayout()
        self.Ivalue = QLabel("  I = (Km"+str(self.i+1)+" + R"+str(self.i+1)+") <<< Kr"+str(self.i+1) +
                             "\n"
                             "\n "+self.formattingBits(self.Km[self.i])+" " 
                                                                        "\n"
                             "\n                                 +                     " 
                                                                        "\n"
                             "\n "+self.formattingBits(self.R[self.i])+"  " 
                                                                       "\n"
                             "\n                                <<<                    "
                                                                       "\n"
                             "\n                              "+ba2base(2, self.Kr[self.i])+" "
                                                               "\n"
                             "\n                                 =                     "
                                                               "\n"
                             "\n"+self.formattingBits(self.I[self.i])+"")

        layoutLabels.addWidget(self.Ivalue)

        sBoxesLayout = QGridLayout()
        Ia = QLabel("Ia")
        Ib = QLabel("Ib")
        Ic = QLabel("Ic")
        Id = QLabel("Id")
        sBoxesLayout.addWidget(Ia, 1, 1)
        sBoxesLayout.addWidget(Ib, 2, 1)
        sBoxesLayout.addWidget(Ic, 3, 1)
        sBoxesLayout.addWidget(Id, 4, 1)
        self.Iabcd = divideITo4Parts(self.I[self.i])
        self.IaValue = QLabel(ba2base(2, self.Iabcd[0]))
        self.IbValue = QLabel(ba2base(2, self.Iabcd[1]))
        self.IcValue = QLabel(ba2base(2, self.Iabcd[2]))
        self.IdValue = QLabel(ba2base(2, self.Iabcd[3]))
        sBoxesLayout.addWidget(self.IaValue, 1, 2)
        sBoxesLayout.addWidget(self.IbValue, 2, 2)
        sBoxesLayout.addWidget(self.IcValue, 3, 2)
        sBoxesLayout.addWidget(self.IdValue, 4, 2)
        self.Sbox1 = QPushButton("Sbox1")
        self.Sbox2 = QPushButton("Sbox2")
        self.Sbox3 = QPushButton("Sbox3")
        self.Sbox4 = QPushButton("Sbox4")
        sBoxesLayout.addWidget(self.Sbox1, 1, 3)
        sBoxesLayout.addWidget(self.Sbox2, 2, 3)
        sBoxesLayout.addWidget(self.Sbox3, 3, 3)
        sBoxesLayout.addWidget(self.Sbox4, 4, 3)
        self.Sbox1Value = QLabel(self.formattingBits(calculatingSboxOutput(1, self.Iabcd[0])))
        self.Sbox2Value = QLabel(self.formattingBits(calculatingSboxOutput(2, self.Iabcd[1])))
        self.Sbox3Value = QLabel(self.formattingBits(calculatingSboxOutput(3, self.Iabcd[2])))
        self.Sbox4Value = QLabel(self.formattingBits(calculatingSboxOutput(4, self.Iabcd[3])))
        sBoxesLayout.addWidget(self.Sbox1Value, 1, 4)
        sBoxesLayout.addWidget(self.Sbox2Value, 2, 4)
        sBoxesLayout.addWidget(self.Sbox3Value, 3, 4)
        sBoxesLayout.addWidget(self.Sbox4Value, 4, 4)

        verticalLayout = QVBoxLayout()
        verticalLayout.addLayout(layoutLabels)
        verticalLayout.addLayout(sBoxesLayout)

        pictureLayout = QVBoxLayout()
        self.labeltab2 = QLabel(self)
        self.pixmaptab2 = QPixmap('UI/images/f1step2.png')
        self.pixmaptab2.scaled(32, 32, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.labeltab2.setPixmap(self.pixmaptab2)
        pictureLayout.addWidget(self.labeltab2)

        layout.addLayout(verticalLayout)
        layout.addLayout(pictureLayout)
        self.setTabText(1, "Step 2")
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QHBoxLayout()
        formLayout = QVBoxLayout()
        self.Fvalue = QLabel("F = ((S1[Ia] ^ S2[Ib]) - S3[Ic]) + S4[Id]"
                             "\n"
                             "\n"+self.formattingBits(calculatingSboxOutput(1, self.Iabcd[0]))+
                             "\n"
                             "\n                           ^"
                             "\n"
                             "\n"+self.formattingBits(calculatingSboxOutput(2, self.Iabcd[1]))+
                             "\n"              
                             "\n                           -"
                             "\n"
                             "\n"+self.formattingBits(calculatingSboxOutput(3, self.Iabcd[2]))+
                             "\n"
                             "\n                           +"
                             "\n"
                             "\n" + self.formattingBits(calculatingSboxOutput(4, self.Iabcd[3])) +
                             "\n"
                             "\n                           ="
                             "\n"
                             "\n" + self.formattingBits(self.f[self.i]))
        formLayout.addWidget(self.Fvalue)

        pictureLayout = QVBoxLayout()
        self.labeltab3 = QLabel(self)
        self.pixmaptab3 = QPixmap('UI/images/f1step3.png')
        self.pixmaptab3.scaled(32, 32, Qt.KeepAspectRatio)
        self.labeltab3.setPixmap(self.pixmaptab3)
        pictureLayout.addWidget(self.labeltab3)

        self.setTabText(2, "Step 3")
        layout.addLayout(formLayout)
        layout.addLayout(pictureLayout)
        self.tab3.setLayout(layout)

    def tab4UI(self):
        layout = QHBoxLayout()
        formLayout = QHBoxLayout()
        self.Llabel = QLabel(" L"+str(self.i+2)+" = R"+str(self.i+1) +
                             "\n"
                             "\nL"+str(self.i+2)+ " = " + self.formattingBits(self.R[self.i + 1])+
                             "\n"
                             "\nR"+str(self.i+2)+" = L"+str(self.i+1) + " ^ F"
                             "\n"
                             "\n"+self.formattingBits(self.L[self.i]) +
                             "\n"
                             "\n                  ^"
                             "\n"
                             "\n"+self.formattingBits(self.f[self.i])+
                             "\n"
                             "\n                  ="
                             "\n"
                             "\n" + self.formattingBits((self.L[self.i] ^ self.f[self.i])))
        formLayout.addWidget(self.Llabel)
        self.plainOrCipherlabel = QLabel("")
        formLayout.addWidget(self.plainOrCipherlabel)

        pictureLayout = QVBoxLayout()
        self.labeltab4 = QLabel(self)
        self.pixmaptab4 = QPixmap('UI/images/f1step4.png')
        self.pixmaptab4.scaled(32, 32, Qt.KeepAspectRatio)
        self.labeltab4.setPixmap(self.pixmaptab4)
        pictureLayout.addWidget(self.labeltab4)

        self.setTabText(3, "Step 4")
        layout.addLayout(formLayout)
        layout.addLayout(pictureLayout)
        self.tab4.setLayout(layout)

    def openSBoxWidget(self, Sbox, Iabcd, title):
        sBoxWidget = SboxWidget(Sbox, Iabcd, title)
        sBoxWidget.exec_()

    def formattingBits(self, bitArray):
        divide = divideKeyTo8Parts(bitArray)

        return ba2base(2, divide[0]) + " " + ba2base(2, divide[1]) + " " + ba2base(2, divide[2]) \
            + " " + ba2base(2, divide[3]) + " " + ba2base(2, divide[4]) + " " + ba2base(2,divide[5]) \
            + " " + ba2base(2, divide[6]) + " " + ba2base(2, divide[7])