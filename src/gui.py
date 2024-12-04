from qgis.PyQt.QtWidgets import *

class BurnMapperDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
    
    def setupUi(self):
        self.layout = QVBoxLayout()
        self.threshold = QDoubleSpinBox()
        self.threshold.setValue(-0.2)
        self.layout.addWidget(self.threshold)
        self.setLayout(self.layout)