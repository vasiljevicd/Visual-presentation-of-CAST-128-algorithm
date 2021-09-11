
from PyQt5.QtWidgets import *
import sys

from UI.mainDialog import MainDialog

app = QApplication(sys.argv)
mainDialog = MainDialog()
mainDialog.show()
app.exec_()

