from PyQt5 import QtWidgets
from .mission_export_format_dialog import Ui_MissionFormat_Dialog

class MissionExportFormat(QtWidgets.QDialog, Ui_MissionFormat_Dialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.create_pushButton.clicked.connect(self.Create)
        self.cancel_pushButton.clicked.connect(self.Cancel)


    def Create(self):
        self.GPKG = self.GPKG_checkBox.isChecked()
        self.SHP = self.SHP_checkBox.isChecked()
        self.accept()

    def Cancel(self):
        self.reject()

    def closeEvent(self, event):
        self.reject()