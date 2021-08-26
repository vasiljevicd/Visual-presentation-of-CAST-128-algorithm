from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton


class ErrorDialog(QDialog):
    def __init__(self, text):
        QDialog.__init__(self)
        self.text = text
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.label = QLabel(self.text)
        self.setWindowTitle("Error!")
        layout.addWidget(self.label)
        self.setLayout(layout)