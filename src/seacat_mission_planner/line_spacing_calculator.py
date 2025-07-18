from PyQt5 import QtWidgets
import math
from.linespacing_calculator_dialog import Ui_LineSpacingCalculatorDialog

class LineSpacingCalculator(QtWidgets.QDialog, Ui_LineSpacingCalculatorDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.Apply_pushButton.clicked.connect(self.Apply)
        self.Cancel_pushButton.clicked.connect(self.Cancel)

        self.Altitude_doubleSpinBox.valueChanged.connect(self.LineSpacingCalculator)
        self.MBESAngle_spinBox.valueChanged.connect(self.LineSpacingCalculator)
        self.Overlap_spinBox.valueChanged.connect(self.LineSpacingCalculator)


    def LineSpacingCalculator(self):
        Height = float(self.Altitude_doubleSpinBox.value())
        MbesAngle = float(self.MBESAngle_spinBox.value())
        Overlap = float(self.Overlap_spinBox.value())
        FullSwath = Height*(math.tan((MbesAngle/2)*math.pi/180))*2
        Overlap = FullSwath * (Overlap/100)
        LineSpacing = round(FullSwath-Overlap,1)
        self.LsCalcResult_doubleSpinBox.setValue(LineSpacing)

    def Apply(self):
        self.LineSpacing = self.LsCalcResult_doubleSpinBox.value()
        self.Height = self.Altitude_doubleSpinBox.value()
        self.MbesAngle= self.MBESAngle_spinBox.value()
        self.accept()

    def Cancel(self):
        self.reject()

    def closeEvent(self, event):
        self.reject()