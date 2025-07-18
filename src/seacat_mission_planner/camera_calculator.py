from PyQt5 import QtWidgets
import math
from.camera_calculator_dialog import Ui_PhotogrammetryCalculatorDialog

class CameraCalculator(QtWidgets.QDialog, Ui_PhotogrammetryCalculatorDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.Apply_pushButton.clicked.connect(self.Apply)
        self.Cancel_pushButton.clicked.connect(self.Cancel)

        self.Altitude_doubleSpinBox.valueChanged.connect(self.CameraCalculator)
        self.Fps_spinBox.valueChanged.connect(self.CameraCalculator)
        self.LongOverlap_spinBox.valueChanged.connect(self.CameraCalculator)
        self.LatOverlap_spinBox.valueChanged.connect(self.CameraCalculator)

    def CameraCalculator(self):
        LatFOV = 70.23
        LongFOV = 47.45

        Height = float(self.Altitude_doubleSpinBox.value())

        Fps = self.Fps_spinBox.value()

        #Calculate line spacing
        LatOverlap = float(self.LatOverlap_spinBox.value())
        LatView = Height * (math.tan((LatFOV / 2) * math.pi / 180)) * 2
        LatOverlapMeter = LatView * (LatOverlap / 100)
        LineSpacing = round(LatView - LatOverlapMeter, 1)
        self.MaxLineSpacing_doubleSpinBox.setValue(LineSpacing)

        #Calculate speed
        LongOverlap = float(self.LongOverlap_spinBox.value())
        LongView = Height * (math.tan((LongFOV / 2) * math.pi / 180)) * 2
        LongOverlapMeter = LongView * (LongOverlap / 100)
        PicDistance = LongView - LongOverlapMeter
        PicIntervalInSec = 1/Fps
        MaxSpeed = round((PicDistance/PicIntervalInSec) * 1.94384,1) #in knots
        self.MaxSpeed_doubleSpinBox.setValue(MaxSpeed)



    def Apply(self):
        self.LineSpacing = self.MaxLineSpacing_doubleSpinBox.value()
        self.Height = self.Altitude_doubleSpinBox.value()
        self.Fps = self.Fps_spinBox.value()
        self.Speed = self.MaxSpeed_doubleSpinBox.value()
        self.accept()

    def Cancel(self):
        self.reject()

    def closeEvent(self, event):
        self.reject()