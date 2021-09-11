from PyQt5.QtWidgets import QVBoxLayout, QDialog
from UI.tabWidgetGeneratingKeys import TabWidgetGeneratingKeys


class GeneratedKeysDialog(QDialog):
    def __init__(self, keysArray, xArray, zArray):
        QDialog.__init__(self)
        self.keysArray = keysArray
        self.xArray = xArray
        self.zArray = zArray
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Generating keys")
        layout = QVBoxLayout()
        tabWidgetLayout = QVBoxLayout()
        self.tabWidget = TabWidgetGeneratingKeys(self.keysArray, self.xArray, self.zArray)
        tabWidgetLayout.addWidget(self.tabWidget)
        layout.addLayout(tabWidgetLayout)
        self.setLayout(layout)
