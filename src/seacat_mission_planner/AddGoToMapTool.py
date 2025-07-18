from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtGui import QColor
from qgis.gui import QgsMapTool, QgsMapToolEmitPoint,QgsSnapIndicator, QgsRubberBand
from qgis.core import QgsWkbTypes

class AddGoToMapTool(QgsMapToolEmitPoint):
    goToCreated = pyqtSignal(list)
    deactivated = pyqtSignal()

    def __init__(self, canvas):
        self.canvas = canvas
        self.lastMissionPoint = None
        self.nextMissionPoint = None
        QgsMapToolEmitPoint.__init__(self, self.canvas)
        self.snapIndicator = QgsSnapIndicator(self.canvas)
        self.snapper = self.canvas.snappingUtils()

        self.rubberBandLine = QgsRubberBand(self.canvas, QgsWkbTypes.LineGeometry)
        self.rubberBandLine.setColor(QColor(255, 0, 0, 100))
        self.rubberBandLine.setWidth(3)

        self.PointList = []

    def canvasMoveEvent(self, e):

        snapMatch = self.snapper.snapToMap(e.pos())
        self.snapIndicator.setMatch(snapMatch)
        self.rubberBandLine.reset(QgsWkbTypes.LineGeometry)
        if self.lastMissionPoint != None:
            self.rubberBandLine.addPoint(self.lastMissionPoint, False)
        for point in self.PointList:
            self.rubberBandLine.addPoint(point,False)
        if self.nextMissionPoint != None:
            self.rubberBandLine.addPoint(self.toMapCoordinates(e.pos()), False)
            self.rubberBandLine.addPoint(self.nextMissionPoint, True)
        else:
            self.rubberBandLine.addPoint(self.toMapCoordinates(e.pos()), True)

    def canvasPressEvent(self, e):
        if e.button() == 1:
            if self.snapIndicator.match().type():
                point = self.snapIndicator.match().point()
                self.snapIndicator.setVisible(False)
            else:
                point = self.toMapCoordinates(e.pos())
            self.PointList.append(point)
        if e.button() == 2:
            self.goToCreated.emit(self.PointList)

    def deactivate(self):
        self.PointList = []
        self.lastMissionPoint = None
        self.nextMissionPoint = None
        self.rubberBandLine.reset(QgsWkbTypes.LineGeometry)
        QgsMapTool.deactivate(self)
        self.deactivated.emit()