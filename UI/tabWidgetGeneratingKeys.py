from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QLabel
from bitarray._util import ba2base

from core.keyGenerator import divideKeyTo16Parts, divideKeyTo4Parts
from core.sboxes import calculatingSboxOutput


class TabWidgetGeneratingKeys(QTabWidget):
    def __init__(self, keysArray, xArray, zArray):
        super(TabWidgetGeneratingKeys, self).__init__()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()
        self.tab8 = QWidget()
        self.keysArray = [None] * 32
        self.xArray = [None] * 5
        self.zArray = [None] * 4
        self.keysArray = keysArray
        self.xArray = xArray
        self.zArray = zArray
        self.addTab(self.tab1, "K1-K4")
        self.addTab(self.tab2, "K5-K8")
        self.addTab(self.tab3, "K9-K12")
        self.addTab(self.tab4, "K13-K16")
        self.addTab(self.tab5, "K17-K20")
        self.addTab(self.tab6, "K21-K24")
        self.addTab(self.tab7, "K25-K28")
        self.addTab(self.tab8, "K29-K32")
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.tab6UI()
        self.tab7UI()
        self.tab8UI()

    def tab1UI(self):
        layoutLabel = QVBoxLayout()
        x = divideKeyTo16Parts(self.xArray[0])
        z = divideKeyTo16Parts(self.zArray[0])
        self.labelTab1 = QLabel('x0x1x2x3x4x5x6x7x8x9xAxBxCxDxExF = ' + self.formatting128Bits(self.xArray[0]) +
                            '\n'
                            '\nz0z1z2z3 = x0x1x2x3 ^ S5[xD] ^ S6[xF] ^ S7[xC] ^ S8[xE] ^ S7[x8]'
                            '\n                  = ' + self.formatting32Bits(self.xArray[0][0:32]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[13])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[15])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[12])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[14])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[8])) +
                            '\n                  = ' + self.formatting32Bits(self.zArray[0][0:32]) +
                            '\n'
                            '\nz4z5z6z7 = x8x9xAxB ^ S5[z0] ^ S6[z2] ^ S7[z1] ^ S8[z3] ^ S8[xA]'
                            '\n                  = ' + self.formatting32Bits(self.xArray[0][32:64]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[0])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[2])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[1])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[3])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[10])) +
                            '\n                  = ' + self.formatting32Bits(self.zArray[0][32:64]) +
                            '\n'
                            '\nz8z9zAzB = xCxDxExF ^ S5[z7] ^ S6[z6] ^ S7[z5] ^ S8[z4] ^ S5[x9]'
                            '\n                  = ' + self.formatting32Bits(self.xArray[0][96:128]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[7])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[6])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[5])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[4])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[9])) +
                            '\n                  = ' + self.formatting32Bits(self.zArray[0][64:96]) +
                            '\n'
                            '\nzCzDzEzF = x4x5x6x7 ^ S5[zA] ^ S6[z9] ^ S7[zB] ^ S8[z8] ^ S6[xB]'
                            '\n                  = ' + self.formatting32Bits(self.xArray[0][32:64]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[10])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[9])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[11])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[8])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[11])) +
                            '\n                  = ' + self.formatting32Bits(self.zArray[0][96:128]) +
                            '\n'
                            '\nz0z1z2z3z4z5z6z7z8z9zAzBzCzDzEzF = ' + self.formatting128Bits(self.zArray[0]) +
                            '\n'
                            '\nK1(Km1)  = S5[z8] ^ S6[z9] ^ S7[z7] ^ S8[z6] ^ S5[z2]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[8])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[9])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[7])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[6])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[2])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[0]) +
                            '\n'
                            '\nK2(Km2)  = S5[zA] ^ S6[zB] ^ S7[z5] ^ S8[z4] ^ S6[z6]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[10])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[11])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[5])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[4])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[6])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[1]) +
                            '\n'
                            '\nK3(Km3)  = S5[zC] ^ S6[zD] ^ S7[z3] ^ S8[z2] ^ S7[z9]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[12])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[13])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[3])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[2])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[9])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[2]) +
                            '\n'
                            '\nK4(Km4)  = S5[zE] ^ S6[zF] ^ S7[z1] ^ S8[z0] ^ S8[zC]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[14])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[15])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[1])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[0])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[13])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[3]))
        layoutLabel.addWidget(self.labelTab1)
        self.setTabText(0, "K1-K4")
        self.tab1.setLayout(layoutLabel)

    def tab2UI(self):
        x = divideKeyTo16Parts(self.xArray[1])
        z = divideKeyTo16Parts(self.zArray[0])
        layoutLabel = QVBoxLayout()
        self.labelTab2 = QLabel('z0z1z2z3z4z5z6z7z8z9zAzBzCzDzEzF = ' + self.formatting128Bits(self.zArray[0]) +
                            '\n'
                            '\nx0x1x2x3 = z8z9zAzB ^ S5[z5] ^ S6[z7] ^ S7[z4] ^ S8[z6] ^ S7[z0]'
                            '\n                  = ' + self.formatting32Bits(self.zArray[0][64:96]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[5])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[7])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[4])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[6])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[0])) +
                            '\n                  = ' + self.formatting32Bits(self.xArray[1][0:32]) +
                            '\n'
                            '\nx4x5x6x7 = z0z1z2z3 ^ S5[x0] ^  S6[x2] ^  S7[x1] ^  S8[x3] ^ S8[z2]'
                            '\n                  = ' + self.formatting32Bits(self.zArray[0][0:32]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[0])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[2])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[1])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[3])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[2])) +
                            '\n                  = ' + self.formatting32Bits(self.xArray[1][32:64]) +
                            '\n'
                            '\nx8x9xAxB = z4z5z6z7 ^ S5[x7] ^ S6[x6] ^ S7[x5] ^  S8[x4] ^  S5[z1]'
                            '\n                  = ' + self.formatting32Bits(self.zArray[0][32:64]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[7])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[6])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[5])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[4])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[1])) +
                            '\n                  = ' + self.formatting32Bits(self.xArray[1][64:96]) +
                            '\n'
                            '\nxCxDxExF = zCzDzEzF ^  S5[xA] ^  S6[x9] ^  S7[xB] ^ S8[x8] ^  S6[z3]'
                            '\n                  = ' + self.formatting32Bits(self.zArray[0][96:128]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[10])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[9])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[11])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[8])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[3])) +
                            '\n                  = ' + self.formatting32Bits(self.xArray[1][96:128]) +
                            '\n'
                            '\nx0x1x2x3x4x5x6x7x8x9xAxBxCxDxExF = ' + self.formatting128Bits(self.xArray[1]) +
                            '\n'
                            '\nK5(Km5)  = S5[x3] ^ S6[x2] ^ S7[xC] ^ S8[xD] ^ S5[x8]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[3])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[2])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[12])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[13])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[8])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[4]) +
                            '\n'
                            '\nK6(Km6)  = S5[x1] ^ S6[x0] ^ S7[xE] ^ S8[xF] ^ S6[xD]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[1])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[0])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[14])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[15])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[13])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[5]) +
                            '\n'
                            '\nK7(Km7)  = S5[x7] ^ S6[x6] ^ S7[x8] ^ S8[x9] ^ S7[x3]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[7])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[6])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[8])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[9])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[3])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[6]) +
                            '\n'
                            '\nK8(Km8)  = S5[x5] ^ S6[x4] ^ S7[xA] ^ S8[xB] ^ S8[x7]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[5])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[4])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[10])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[11])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[7])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[7]))
        layoutLabel.addWidget(self.labelTab2)
        self.setTabText(1, "K5-K8")
        self.tab2.setLayout(layoutLabel)

    def tab3UI(self):
        x = divideKeyTo16Parts(self.xArray[1])
        z = divideKeyTo16Parts(self.zArray[1])
        layoutLabel = QVBoxLayout()
        self.labelTab3 = QLabel('x0x1x2x3x4x5x6x7x8x9xAxBxCxDxExF = ' + self.formatting128Bits(self.xArray[1]) +
                            '\n'
                            '\nz0z1z2z3 = x0x1x2x3 ^ S5[xD] ^ S6[xF] ^ S7[xC] ^ S8[xE] ^ S7[x8]'
                            '\n                  = ' + self.formatting32Bits(self.xArray[1][0:32]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[13])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[15])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[12])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[14])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[8])) +
                            '\n                  = ' + self.formatting32Bits(self.zArray[1][0:32]) +
                            '\n'
                            '\nz4z5z6z7 = x8x9xAxB ^ S5[z0] ^ S6[z2] ^ S7[z1] ^ S8[z3] ^ S8[xA]'
                            '\n                  = ' + self.formatting32Bits(self.xArray[1][32:64]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[0])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[2])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[1])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[3])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[10])) +
                            '\n                  = ' + self.formatting32Bits(self.zArray[1][32:64]) +
                            '\n'
                            '\nz8z9zAzB = xCxDxExF ^ S5[z7] ^ S6[z6] ^ S7[z5] ^ S8[z4] ^ S5[x9]'
                            '\n                  = ' + self.formatting32Bits(self.xArray[1][96:128]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[7])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[6])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[5])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[4])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[9])) +
                            '\n                  = ' + self.formatting32Bits(self.zArray[1][64:96]) +
                            '\n'
                            '\nzCzDzEzF = x4x5x6x7 ^ S5[zA] ^ S6[z9] ^ S7[zB] ^ S8[z8] ^ S6[xB]'
                            '\n                  = ' + self.formatting32Bits(self.xArray[1][32:64]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[10])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[9])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[11])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[8])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[11])) +
                            '\n                  = ' + self.formatting32Bits(self.zArray[1][96:128]) +
                            '\n'
                            '\nz0z1z2z3z4z5z6z7z8z9zAzBzCzDzEzF = ' + self.formatting128Bits(self.zArray[1]) +
                            '\n'
                            '\nK9(Km9)  = S5[z3] ^ S6[z2] ^ S7[zC] ^ S8[zD] ^ S5[z9]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[3])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[2])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[12])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[13])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[9])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[8]) +
                            '\n'
                            '\nK10(Km10) = S5[z1] ^ S6[z0] ^ S7[zE] ^ S8[zF] ^ S6[zC]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[1])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[0])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[14])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[15])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[12])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[9]) +
                            '\n'
                            '\nK11(Km11) = S5[z7] ^ S6[z6] ^ S7[z8] ^ S8[z9] ^ S7[z2]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[7])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[6])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[8])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[9])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[2])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[10]) +
                            '\n'
                            '\nK12(Km12) = S5[z5] ^ S6[z4] ^ S7[zA] ^ S8[zB] ^ S8[z6]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[5])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[4])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[10])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[11])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[6])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[11]))
        layoutLabel.addWidget(self.labelTab3)
        self.setTabText(2, "K9-K12")
        self.tab3.setLayout(layoutLabel)

    def tab4UI(self):
        x = divideKeyTo16Parts(self.xArray[2])
        z = divideKeyTo16Parts(self.zArray[1])
        layoutLabel = QVBoxLayout()
        self.labelTab4 = QLabel('z0z1z2z3z4z5z6z7z8z9zAzBzCzDzEzF = ' + self.formatting128Bits(self.zArray[1]) +
                            '\n'
                            '\nx0x1x2x3 = z8z9zAzB ^ S5[z5] ^ S6[z7] ^ S7[z4] ^ S8[z6] ^ S7[z0]'
                            '\n                  = ' + self.formatting32Bits(self.zArray[1][64:96]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[5])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[7])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[4])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[6])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, z[0])) +
                            '\n                  = ' + self.formatting32Bits(self.xArray[2][0:32]) +
                            '\n'
                            '\nx4x5x6x7 = z0z1z2z3 ^ S5[x0] ^  S6[x2] ^  S7[x1] ^  S8[x3] ^ S8[z2]'
                            '\n                  = ' + self.formatting32Bits(self.zArray[1][0:32]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[0])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[2])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[1])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[3])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, z[2])) +
                            '\n                  = ' + self.formatting32Bits(self.xArray[2][32:64]) +
                            '\n'
                            '\nx8x9xAxB = z4z5z6z7 ^ S5[x7] ^ S6[x6] ^ S7[x5] ^  S8[x4] ^  S5[z1]'
                            '\n                  = ' + self.formatting32Bits(self.zArray[1][32:64]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[7])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[6])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[5])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[4])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, z[1])) +
                            '\n                  = ' + self.formatting32Bits(self.xArray[2][64:96]) +
                            '\n'
                            '\nxCxDxExF = zCzDzEzF ^  S5[xA] ^  S6[x9] ^  S7[xB] ^ S8[x8] ^  S6[z3]'
                            '\n                  = ' + self.formatting32Bits(self.zArray[1][96:128]) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[10])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[9])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[11])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[8])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, z[3])) +
                            '\n                  = ' + self.formatting32Bits(self.xArray[2][96:128]) +
                            '\n'
                            '\nx0x1x2x3x4x5x6x7x8x9xAxBxCxDxExF = ' + self.formatting128Bits(self.xArray[2]) +
                            '\n'
                            '\nK13(Km13) = S5[x8] ^ S6[x9] ^ S7[x7] ^ S8[x6] ^ S5[x3]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[8])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[9])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[7])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[6])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(5, x[3])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[12]) +
                            '\n'
                            '\nK14(Km14) = S5[xA] ^ S6[xB] ^ S7[x5] ^ S8[x4] ^ S6[x7]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[10])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[11])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[5])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[4])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[7])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[13]) +
                            '\n'
                            '\nK15(Km15) = S5[xC] ^ S6[xD] ^ S7[x3] ^ S8[x2] ^ S7[x8]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[12])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[13])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[3])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[2])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[8])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[14]) +
                            '\n'
                            '\nK16(Km16) = S5[xE] ^ S6[xF] ^ S7[x1] ^ S8[x0] ^ S8[xD]'
                            '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[14])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(6, x[15])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(7, x[1])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[0])) + ' ^ '
                            + self.formatting32Bits(calculatingSboxOutput(8, x[12])) +
                            '\n                 = ' + self.formatting32Bits(self.keysArray[15]))
        layoutLabel.addWidget(self.labelTab4)
        self.setTabText(3, "K13-K16")
        self.tab4.setLayout(layoutLabel)

    def tab5UI(self):
        layoutLabel = QVBoxLayout()
        x = divideKeyTo16Parts(self.xArray[2])
        z = divideKeyTo16Parts(self.zArray[2])
        self.labelTab5 = QLabel('x0x1x2x3x4x5x6x7x8x9xAxBxCxDxExF = ' + self.formatting128Bits(self.xArray[2]) +
                                '\n'
                                '\nz0z1z2z3 = x0x1x2x3 ^ S5[xD] ^ S6[xF] ^ S7[xC] ^ S8[xE] ^ S7[x8]'
                                '\n                  = ' + self.formatting32Bits(self.xArray[2][0:32]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[13])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[15])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[12])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[14])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[8])) +
                                '\n                  = ' + self.formatting32Bits(self.zArray[2][0:32]) +
                                '\n'
                                '\nz4z5z6z7 = x8x9xAxB ^ S5[z0] ^ S6[z2] ^ S7[z1] ^ S8[z3] ^ S8[xA]'
                                '\n                  = ' + self.formatting32Bits(self.xArray[2][32:64]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[0])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[2])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[1])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[3])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[10])) +
                                '\n                  = ' + self.formatting32Bits(self.zArray[2][32:64]) +
                                '\n'
                                '\nz8z9zAzB = xCxDxExF ^ S5[z7] ^ S6[z6] ^ S7[z5] ^ S8[z4] ^ S5[x9]'
                                '\n                  = ' + self.formatting32Bits(self.xArray[2][96:128]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[7])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[6])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[5])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[4])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[9])) +
                                '\n                  = ' + self.formatting32Bits(self.zArray[2][64:96]) +
                                '\n'
                                '\nzCzDzEzF = x4x5x6x7 ^ S5[zA] ^ S6[z9] ^ S7[zB] ^ S8[z8] ^ S6[xB]'
                                '\n                  = ' + self.formatting32Bits(self.xArray[2][32:64]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[10])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[9])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[11])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[8])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[11])) +
                                '\n                  = ' + self.formatting32Bits(self.zArray[2][96:128]) +
                                '\n'
                                '\nz0z1z2z3z4z5z6z7z8z9zAzBzCzDzEzF = ' + self.formatting128Bits(self.zArray[2]) +
                                '\n'
                                '\nK17(Kr1)  = S5[z8] ^ S6[z9] ^ S7[z7] ^ S8[z6] ^ S5[z2]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[8])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[9])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[7])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[6])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[2])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[16]) +
                                '\n'
                                '\nK18(Kr2)  = S5[zA] ^ S6[zB] ^ S7[z5] ^ S8[z4] ^ S6[z6]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[10])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[11])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[5])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[4])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[6])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[17]) +
                                '\n'
                                '\nK19(Kr3)  = S5[zC] ^ S6[zD] ^ S7[z3] ^ S8[z2] ^ S7[z9]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[12])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[13])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[3])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[2])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[9])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[18]) +
                                '\n'
                                '\nK20(Kr4)  = S5[zE] ^ S6[zF] ^ S7[z1] ^ S8[z0] ^ S8[zC]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[14])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[15])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[1])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[0])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[13])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[19]))
        layoutLabel.addWidget(self.labelTab5)
        self.setTabText(4, "K17-K20")
        self.tab5.setLayout(layoutLabel)

    def tab6UI(self):
        x = divideKeyTo16Parts(self.xArray[3])
        z = divideKeyTo16Parts(self.zArray[2])
        layoutLabel = QVBoxLayout()
        self.labelTab6 = QLabel('z0z1z2z3z4z5z6z7z8z9zAzBzCzDzEzF = ' + self.formatting128Bits(self.zArray[2]) +
                                '\n'
                                '\nx0x1x2x3 = z8z9zAzB ^ S5[z5] ^ S6[z7] ^ S7[z4] ^ S8[z6] ^ S7[z0]'
                                '\n                  = ' + self.formatting32Bits(self.zArray[2][64:96]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[5])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[7])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[4])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[6])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[0])) +
                                '\n                  = ' + self.formatting32Bits(self.xArray[3][0:32]) +
                                '\n'
                                '\nx4x5x6x7 = z0z1z2z3 ^ S5[x0] ^  S6[x2] ^  S7[x1] ^  S8[x3] ^ S8[z2]'
                                '\n                  = ' + self.formatting32Bits(self.zArray[2][0:32]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[0])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[2])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[1])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[3])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[2])) +
                                '\n                  = ' + self.formatting32Bits(self.xArray[3][32:64]) +
                                '\n'
                                '\nx8x9xAxB = z4z5z6z7 ^ S5[x7] ^ S6[x6] ^ S7[x5] ^  S8[x4] ^  S5[z1]'
                                '\n                  = ' + self.formatting32Bits(self.zArray[2][32:64]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[7])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[6])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[5])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[4])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[1])) +
                                '\n                  = ' + self.formatting32Bits(self.xArray[3][64:96]) +
                                '\n'
                                '\nxCxDxExF = zCzDzEzF ^  S5[xA] ^  S6[x9] ^  S7[xB] ^ S8[x8] ^  S6[z3]'
                                '\n                  = ' + self.formatting32Bits(self.zArray[2][96:128]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[10])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[9])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[11])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[8])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[3])) +
                                '\n                  = ' + self.formatting32Bits(self.xArray[3][96:128]) +
                                '\n'
                                '\nx0x1x2x3x4x5x6x7x8x9xAxBxCxDxExF = ' + self.formatting128Bits(self.xArray[3]) +
                                '\n'
                                '\nK21(Kr5)  = S5[x3] ^ S6[x2] ^ S7[xC] ^ S8[xD] ^ S5[x8]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[3])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[2])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[12])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[13])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[8])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[20]) +
                                '\n'
                                '\nK22(Kr6)  = S5[x1] ^ S6[x0] ^ S7[xE] ^ S8[xF] ^ S6[xD]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[1])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[0])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[14])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[15])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[13])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[21]) +
                                '\n'
                                '\nK23(Kr7)  = S5[x7] ^ S6[x6] ^ S7[x8] ^ S8[x9] ^ S7[x3]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[7])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[6])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[8])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[9])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[3])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[22]) +
                                '\n'
                                '\nK24(Kr8)  = S5[x5] ^ S6[x4] ^ S7[xA] ^ S8[xB] ^ S8[x7]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[5])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[4])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[10])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[11])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[7])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[23]))
        layoutLabel.addWidget(self.labelTab6)
        self.setTabText(5, "K21-K24")
        self.tab6.setLayout(layoutLabel)

    def tab7UI(self):
        x = divideKeyTo16Parts(self.xArray[3])
        z = divideKeyTo16Parts(self.zArray[3])
        layoutLabel = QVBoxLayout()
        self.labelTab7 = QLabel('x0x1x2x3x4x5x6x7x8x9xAxBxCxDxExF = ' + self.formatting128Bits(self.xArray[3]) +
                                '\n'
                                '\nz0z1z2z3 = x0x1x2x3 ^ S5[xD] ^ S6[xF] ^ S7[xC] ^ S8[xE] ^ S7[x8]'
                                '\n                  = ' + self.formatting32Bits(self.xArray[3][0:32]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[13])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[15])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[12])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[14])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[8])) +
                                '\n                  = ' + self.formatting32Bits(self.zArray[3][0:32]) +
                                '\n'
                                '\nz4z5z6z7 = x8x9xAxB ^ S5[z0] ^ S6[z2] ^ S7[z1] ^ S8[z3] ^ S8[xA]'
                                '\n                  = ' + self.formatting32Bits(self.xArray[3][32:64]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[0])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[2])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[1])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[3])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[10])) +
                                '\n                  = ' + self.formatting32Bits(self.zArray[3][32:64]) +
                                '\n'
                                '\nz8z9zAzB = xCxDxExF ^ S5[z7] ^ S6[z6] ^ S7[z5] ^ S8[z4] ^ S5[x9]'
                                '\n                  = ' + self.formatting32Bits(self.xArray[3][96:128]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[7])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[6])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[5])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[4])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[9])) +
                                '\n                  = ' + self.formatting32Bits(self.zArray[3][64:96]) +
                                '\n'
                                '\nzCzDzEzF = x4x5x6x7 ^ S5[zA] ^ S6[z9] ^ S7[zB] ^ S8[z8] ^ S6[xB]'
                                '\n                  = ' + self.formatting32Bits(self.xArray[3][32:64]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[10])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[9])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[11])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[8])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[11])) +
                                '\n                  = ' + self.formatting32Bits(self.zArray[3][96:128]) +
                                '\n'
                                '\nz0z1z2z3z4z5z6z7z8z9zAzBzCzDzEzF = ' + self.formatting128Bits(self.zArray[3]) +
                                '\n'
                                '\nK25(Kr9)  = S5[z3] ^ S6[z2] ^ S7[zC] ^ S8[zD] ^ S5[z9]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[3])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[2])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[12])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[13])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[9])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[24]) +
                                '\n'
                                '\nK26(Kr10) = S5[z1] ^ S6[z0] ^ S7[zE] ^ S8[zF] ^ S6[zC]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[1])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[0])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[14])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[15])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[12])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[25]) +
                                '\n'
                                '\nK27(Kr11) = S5[z7] ^ S6[z6] ^ S7[z8] ^ S8[z9] ^ S7[z2]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[7])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[6])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[8])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[9])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[2])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[26]) +
                                '\n'
                                '\nK28(Kr12) = S5[z5] ^ S6[z4] ^ S7[zA] ^ S8[zB] ^ S8[z6]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, z[5])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[4])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[10])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[11])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[6])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[27]))
        layoutLabel.addWidget(self.labelTab7)
        self.setTabText(6, "K25-K28")
        self.tab7.setLayout(layoutLabel)

    def tab8UI(self):
        x = divideKeyTo16Parts(self.xArray[4])
        z = divideKeyTo16Parts(self.zArray[3])
        layoutLabel = QVBoxLayout()
        self.labelTab8 = QLabel('z0z1z2z3z4z5z6z7z8z9zAzBzCzDzEzF = ' + self.formatting128Bits(self.zArray[3]) +
                                '\n'
                                '\nx0x1x2x3 = z8z9zAzB ^ S5[z5] ^ S6[z7] ^ S7[z4] ^ S8[z6] ^ S7[z0]'
                                '\n                  = ' + self.formatting32Bits(self.zArray[3][64:96]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[5])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[7])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[4])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[6])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, z[0])) +
                                '\n                  = ' + self.formatting32Bits(self.xArray[4][0:32]) +
                                '\n'
                                '\nx4x5x6x7 = z0z1z2z3 ^ S5[x0] ^  S6[x2] ^  S7[x1] ^  S8[x3] ^ S8[z2]'
                                '\n                  = ' + self.formatting32Bits(self.zArray[3][0:32]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[0])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[2])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[1])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[3])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, z[2])) +
                                '\n                  = ' + self.formatting32Bits(self.xArray[4][32:64]) +
                                '\n'
                                '\nx8x9xAxB = z4z5z6z7 ^ S5[x7] ^ S6[x6] ^ S7[x5] ^  S8[x4] ^  S5[z1]'
                                '\n                  = ' + self.formatting32Bits(self.zArray[3][32:64]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[7])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[6])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[5])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[4])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, z[1])) +
                                '\n                  = ' + self.formatting32Bits(self.xArray[4][64:96]) +
                                '\n'
                                '\nxCxDxExF = zCzDzEzF ^  S5[xA] ^  S6[x9] ^  S7[xB] ^ S8[x8] ^  S6[z3]'
                                '\n                  = ' + self.formatting32Bits(self.zArray[3][96:128]) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[10])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[9])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[11])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[8])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, z[3])) +
                                '\n                  = ' + self.formatting32Bits(self.xArray[4][96:128]) +
                                '\n'
                                '\nx0x1x2x3x4x5x6x7x8x9xAxBxCxDxExF = ' + self.formatting128Bits(self.xArray[4]) +
                                '\n'
                                '\nK29(Kr13) = S5[x8] ^ S6[x9] ^ S7[x7] ^ S8[x6] ^ S5[x3]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[8])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[9])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[7])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[6])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(5, x[3])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[28]) +
                                '\n'
                                '\nK30(Kr14) = S5[xA] ^ S6[xB] ^ S7[x5] ^ S8[x4] ^ S6[x7]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[10])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[11])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[5])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[4])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[7])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[29]) +
                                '\n'
                                '\nK31(Kr15) = S5[xC] ^ S6[xD] ^ S7[x3] ^ S8[x2] ^ S7[x8]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[12])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[13])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[3])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[2])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[8])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[30]) +
                                '\n'
                                '\nK32(Kr16) = S5[xE] ^ S6[xF] ^ S7[x1] ^ S8[x0] ^ S8[xD]'
                                '\n                 = ' + self.formatting32Bits(calculatingSboxOutput(5, x[14])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(6, x[15])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(7, x[1])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[0])) + ' ^ '
                                + self.formatting32Bits(calculatingSboxOutput(8, x[12])) +
                                '\n                 = ' + self.formatting32Bits(self.keysArray[31]))
        layoutLabel.addWidget(self.labelTab8)
        self.setTabText(7, "K29-K32")
        self.tab8.setLayout(layoutLabel)

    def formatting128Bits(self,bitArray):
        divide = divideKeyTo16Parts(bitArray)

        return ba2base(2, divide[0]) + " " + ba2base(2, divide[1]) + " " + ba2base(2, divide[2]) \
               + " " + ba2base(2, divide[3]) + " " + ba2base(2, divide[4]) + " " + ba2base(2, divide[5]) \
               + " " + ba2base(2, divide[6]) + " " + ba2base(2, divide[7]) + " " \
               + ba2base(2, divide[8]) + " " + ba2base(2, divide[9]) + " " + ba2base(2, divide[10]) \
               + " " + ba2base(2, divide[11]) + " " + ba2base(2, divide[12]) + " " + ba2base(2, divide[13]) \
               + " " + ba2base(2, divide[14]) + " " + ba2base(2, divide[15])

    def formatting32Bits(self,bitArray):
        divide = divideKeyTo4Parts(bitArray)

        return ba2base(2, divide[0]) + " " + ba2base(2, divide[1]) + " " + ba2base(2, divide[2]) \
               + " " + ba2base(2, divide[3])
