from PyQt5 import QtWidgets
from.wingline_creator_dialog import Ui_WinglineCreator

class WingLineCreator(QtWidgets.QDialog, Ui_WinglineCreator):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.create_pushButton.clicked.connect(self.Create)
        self.cancel_pushButton.clicked.connect(self.Cancel)
        self.stbd_lines_spinBox.setValue(10)
        self.port_lines_spinBox.setValue(10)

    def Create(self):
        self.Offset = self.offset_doubleSpinBox.value()
        self.NStbdLines = self.stbd_lines_spinBox.value()
        self.NPortLines = self.port_lines_spinBox.value()
        self.FirstTurn = self.first_turn_comboBox.currentText()
        self.InvertLine = self.Invert_checkBox.isChecked()
        self.accept()

    def Cancel(self):
        self.reject()

    def closeEvent(self, event):
        self.reject()
