from PyQt5 import QtWidgets
from.resurface_planner_dialog import Ui_ResurfacePlanner

class ResurfacePlanner(QtWidgets.QDialog, Ui_ResurfacePlanner):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.create_pushButton.clicked.connect(self.Create)
        self.cancel_pushButton.clicked.connect(self.Cancel)


    def Create(self):
        self.ResurfaceDistance = self.resurface_distance_spinBox.value()
        self.Fig8Distance = self.fig8_distance_spinBox.value()
        self.StbyTime = self.surface_stby_spinBox.value()
        self.Fig8RunIn = self.run_InOut_fig8_spinBox.value()
        self.Fig8RunOut = self.run_InOut_fig8_spinBox.value()
        self.ResurfaceRunIn = self.run_InOut_resurface_spinBox.value()
        self.ResurfaceRunOut = self.run_InOut_resurface_spinBox.value()
        self.TurnSide = self.turn_dir_comboBox.currentText()
        self.Resurface = self.resurface_checkBox.isChecked()
        self.Fig8 = self.fig8_checkBox.isChecked()
        self.LoopsOnAC = self.loop_checkBox.isChecked()
        self.LoopsRunIn = self.run_InOut_loop_spinBox.value()
        self.LoopsRunOut = self.run_InOut_loop_spinBox.value()
        self.LoopsMaxAC = self.maxAC_distance_spinBox.value()
        self.LineRunIn = self.run_In_line_spinBox_5.value()
        self.LineRunOut = self.run_Out_line_spinBox.value()
        self.accept()

    def Cancel(self):
        self.reject()

    def closeEvent(self, event):
        self.reject()