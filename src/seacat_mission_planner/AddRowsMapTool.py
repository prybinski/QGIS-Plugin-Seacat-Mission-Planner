from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtGui import QColor
from qgis.core import QgsPointXY, QgsRectangle, QgsWkbTypes,QgsCoordinateReferenceSystem,QgsProject,QgsCoordinateTransform
from qgis.gui import QgsMapTool, QgsMapToolEmitPoint, QgsRubberBand,QgsSnapIndicator
import math
import numpy


class AddRowsMapTool(QgsMapToolEmitPoint):
    rectangleCreated = pyqtSignal(list)
    deactivated = pyqtSignal()

    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)

        self.rubberBandPoly = QgsRubberBand(self.canvas, QgsWkbTypes.PolygonGeometry)
        self.rubberBandPoly.setColor(QColor(255, 0, 0, 100))
        self.rubberBandPoly.setWidth(2)

        self.rubberBandLine = QgsRubberBand(self.canvas, QgsWkbTypes.LineGeometry)
        self.rubberBandLine.setColor(QColor(255, 0, 0, 100))
        self.rubberBandLine.setWidth(3)

        self.snapIndicator = QgsSnapIndicator(self.canvas)
        self.snapper = self.canvas.snappingUtils()

        self.reset()

    def reset(self):
        self.point1LatLon = None
        self.point2LatLon = None
        self.point3LatLon = None
        self.point4LatLon = None

        self.rubberBandPoly.reset(QgsWkbTypes.PolygonGeometry)
        self.rubberBandLine.reset(QgsWkbTypes.LineGeometry)

    def canvasPressEvent(self, e):
        if e.button() == 2:
            self.rectangleCreated.emit([])
        else:
            self.UpdateTransformation()
            if self.snapIndicator.match().type():
                point = self.snapIndicator.match().point()
                self.snapIndicator.setVisible(False)
            else:
                point = self.toMapCoordinates(e.pos())

            if self.point1LatLon == None:
                self.point1MapCRS = point
                self.point1LatLon = self.xformMapToWGS84.transform(self.point1MapCRS)
                self.EPSG = self.get_utm_zoneEPSG(self.point1LatLon.x() ,self.point1LatLon.y())
                self.Update2ndTransformation(self.EPSG)
                self.point1UTM = self.xformWGS84ToUTM.transform(self.point1LatLon)
                return

            elif self.point2LatLon == None:
                self.point2MapCRS = point
                self.point2LatLon = self.xformMapToWGS84.transform(self.point2MapCRS)
                self.point2UTM = self.xformWGS84ToUTM.transform(self.point2LatLon)
                return

            else:
                self.point3MapCRS = point
                self.point3UTM = self.xformMapToUTM.transform(self.point3MapCRS)
                a = self.findRect()
                if a == True:
                    self.rectangleCreated.emit([(self.point1LatLon,self.point1UTM),(self.point2LatLon,self.point2UTM),
                                                (self.point3LatLon,self.point3UTM),(self.point4LatLon,self.point4UTM),self.EPSG,self.side])

    def canvasMoveEvent(self, e):
        if self.point1LatLon == None:
            snapMatch = self.snapper.snapToMap(e.pos())
            self.snapIndicator.setMatch(snapMatch)
            return
        if self.point2LatLon == None:
            snapMatch = self.snapper.snapToMap(e.pos())
            self.snapIndicator.setMatch(snapMatch)
            self.rubberBandLine.reset(QgsWkbTypes.LineGeometry)
            self.showLine(self.point1MapCRS,self.toMapCoordinates(e.pos()))
            return
        else:
            snapMatch = self.snapper.snapToMap(e.pos())
            self.snapIndicator.setMatch(snapMatch)
            self.rubberBandLine.reset(QgsWkbTypes.LineGeometry)
            self.point3MapCRS = self.toMapCoordinates(e.pos())
            self.point3UTM = self.xformMapToUTM.transform(self.point3MapCRS)

            self.showRect()

    def showRect(self):
        self.rubberBandPoly.reset(QgsWkbTypes.PolygonGeometry)
        a = self.findRect()
        if a == True:
            self.rubberBandPoly.addPoint(self.point1MapCRS,False)
            self.rubberBandPoly.addPoint(self.point2MapCRS, False)
            self.rubberBandPoly.addPoint(self.point3MapCRS, False)
            self.rubberBandPoly.addPoint(self.point4MapCRS, True)
            self.rubberBandPoly.show()

    def showLine(self,startPoint, endPoint):
        self.rubberBandLine.reset(QgsWkbTypes.LineGeometry)
        if startPoint.x() == endPoint.x() or startPoint.y() == endPoint.y():
            return
        self.rubberBandLine.addPoint(startPoint,False)
        self.rubberBandLine.addPoint(endPoint, True)
        self.rubberBandLine.show()

    def UpdateTransformation(self):
        crsDest = QgsCoordinateReferenceSystem("EPSG:4326")
        crsOrig = QgsProject.instance().crs()
        transformContext = QgsProject.instance().transformContext()
        self.xformMapToWGS84 = QgsCoordinateTransform(crsOrig, crsDest, transformContext)

    def Update2ndTransformation(self,EPSG):
        crsDest = QgsCoordinateReferenceSystem(EPSG)
        crsOrig = QgsCoordinateReferenceSystem("EPSG:4326")
        transformContext = QgsProject.instance().transformContext()
        self.xformWGS84ToUTM = QgsCoordinateTransform(crsOrig, crsDest, transformContext)
        crsDest = QgsCoordinateReferenceSystem(EPSG)
        crsOrig = QgsProject.instance().crs()
        transformContext = QgsProject.instance().transformContext()
        self.xformMapToUTM = QgsCoordinateTransform(crsOrig, crsDest, transformContext)

    def get_utm_zoneEPSG(self,longitude,latitude):
        Zone = str((int(1 + (longitude + 180.0) / 6.0)))

        if (latitude < 0.0):
            NorthOrSouth = '7'
        else:
            NorthOrSouth = '6'

        return('EPSG:32'+NorthOrSouth+Zone)

    def findRect(self):
        UTMBearing12 = 90-math.degrees(math.atan2((self.point2UTM.y()-self.point1UTM.y()),(self.point2UTM.x()-self.point1UTM.x())))
        if UTMBearing12 < 0.0:
            UTMBearing12 += 360.0

        LeftOright = (self.point2UTM.x() - self.point1UTM.x() ) * (self.point3UTM.y() - self.point1UTM.y()) \
                     - (self.point2UTM.y() - self.point1UTM.y() ) * (self.point3UTM.x() - self.point1UTM.x() )
        if LeftOright != 0.0:
            if LeftOright >0:
                AngletoAdd = -90
                self.side = 'left'
            else:
                AngletoAdd = 90
                self.side = 'right'

            UTMBearing23 = UTMBearing12+AngletoAdd
            if UTMBearing23 < 0.0:
                UTMBearing23 += 360.0
            elif UTMBearing23 > 360.0:
                UTMBearing23 = UTMBearing23 - 360.0
            UTMBearing23 = math.radians(UTMBearing23)

            P1 = (self.point1UTM.x(),self.point1UTM.y())
            P1 = numpy.asarray(P1)
            P2 = (self.point2UTM.x(), self.point2UTM.y())
            P2 = numpy.asarray(P2)
            P3 = (self.point3UTM.x(), self.point3UTM.y())
            P3 = numpy.asarray(P3)
            d = abs(numpy.cross(P2-P1,P1-P3)/numpy.linalg.norm(P2-P1))

            x = self.point2UTM.x()+(d * math.sin((UTMBearing23)))
            y = self.point2UTM.y() + (d * math.cos((UTMBearing23)))
            self.point3UTM = QgsPointXY(x,y)
            self.point3MapCRS = self.xformMapToUTM.transform(self.point3UTM, QgsCoordinateTransform.ReverseTransform)
            self.point3LatLon = self.xformMapToWGS84.transform(self.point3MapCRS)

            x = self.point1UTM.x() + (d * math.sin((UTMBearing23)))
            y = self.point1UTM.y() + (d * math.cos((UTMBearing23)))
            self.point4UTM = QgsPointXY(x, y)
            self.point4MapCRS = self.xformMapToUTM.transform(self.point4UTM, QgsCoordinateTransform.ReverseTransform)
            self.point4LatLon = self.xformMapToWGS84.transform(self.point4MapCRS)
            return True
        else:
            return False



    def deactivate(self):
        self.reset()
        QgsMapTool.deactivate(self)
        self.deactivated.emit()