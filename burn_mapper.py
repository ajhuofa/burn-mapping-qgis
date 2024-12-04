from qgis.PyQt.QtWidgets import QAction
from qgis.core import *
from .src.process import process_burn_area, clean_polygon_features
from .src.gui import BurnMapperDialog

class BurnMapperPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.dialog = BurnMapperDialog()
        
    def initGui(self):
        self.action = QAction('Burn Mapper', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        
    def run(self):
        if self.dialog.exec_():
            layer = self.iface.activeLayer()
            if layer:
                threshold = self.dialog.threshold.value()
                burns = process_burn_area(layer.source(), None, threshold)
                clean_polygon_features(burns)