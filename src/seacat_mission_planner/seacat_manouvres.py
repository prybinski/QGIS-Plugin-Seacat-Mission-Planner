
class Acoms:
    def __init__(self,Active,Interval,Repetitions,InCurveOnly):
        self.Active = Active
        self.Interval = Interval
        self.Repetitions = Repetitions
        self.InCurveOnly = InCurveOnly

class MBES:
    def __init__(self,Active,OnLinesOnly,Angle,OpMode,GateMode,UpGate,LowGate,BeamDistribution,TxFrequency,TxBandwith,TxAmplitude,TxSweepLenght,TxMatchFilter,BeamNumber):
        self.Active = Active
        self.OnLinesOnly = OnLinesOnly
        self.Angle = Angle
        self.OpMode = OpMode
        self.GateMode = GateMode
        self.UpGate = UpGate
        self.LowGate = LowGate
        self.BeamDistribution = BeamDistribution
        self.TxFrequency = TxFrequency
        self.TxBandwith = TxBandwith
        self.TxAmplitude = TxAmplitude
        self.TxSweepLenght = TxSweepLenght
        self.TxMatchFilter = TxMatchFilter
        self.BeamNumber = BeamNumber

class SSS:
    def __init__(self,Active,OnLinesOnly,Range,OpMode,Gain):
        self.Active = Active
        self.OnLinesOnly = OnLinesOnly
        self.Range = Range
        self.OpMode = OpMode
        self.Gain = Gain

class SBP:
    def __init__(self,Active,OnLinesOnly,Range,LFGain,LFTreshold,LFContrast,HFGain,HFTreshold,HFContrast):
        self.Active = Active
        self.Range = Range
        self.LFGain = LFGain
        self.LFTreshold = LFTreshold
        self.LFContrast = LFContrast
        self.HFGain = HFGain
        self.HFTreshold = HFTreshold
        self.HFContrast = HFContrast
        self.OnLinesOnly = OnLinesOnly

class Camera:
    def __init__(self,Active,Framerate,ShowVideo,Gain,Format,Compression,ShutterTime,Strobe,StrobeIntensity,OnLinesOnly):
        self.Active = Active
        self.Framerate = Framerate
        self.ShowVideo = ShowVideo
        self.Format = Format
        self.Gain = Gain
        self.Compression = Compression
        self.ShutterTime = ShutterTime
        self.Strobe = Strobe
        self.StrobeIntensity = StrobeIntensity
        self.OnLinesOnly = OnLinesOnly

class MAG:
    def __init__(self,Active,OnLinesOnly):
        self.Active = Active
        self.OnLinesOnly = OnLinesOnly

class PlanBlue:
    def __init__(self,Active,OnLinesOnly):
        self.Active = Active
        self.OnLinesOnly = OnLinesOnly

class OAS:
    def __init__(self,Active):
        self.Active = Active

class StationKeeping:
    def __init__(self,Point,MBES,SSS,SBP,Mag,PlanBlue,Camera,OAS,Speed,Height,Acoms,Duration,Name):
        self.DestPointX = Point.x()
        self.DestPointY = Point.y()
        self.Height = Height
        self.Duration = Duration
        self.Speed = Speed
        self.MBES = MBES
        self.SSS = SSS
        self.SBP = SBP
        self.Mag = Mag
        self.PlanBlue = PlanBlue
        self.Camera = Camera
        self.OAS = OAS
        self.Acoms = Acoms
        self.InCurve = True
        self.type = 'SK'
        self.Name = Name

class GoTo:
    def __init__(self,Point,MBES,SSS,SBP,Mag,PlanBlue,Camera,OAS,Speed,Height,Acoms,InCurve,IsRunInRunOutPoint,Name):
        self.DestPointX = Point.x()
        self.DestPointY = Point.y()
        self.MBES = MBES
        self.SSS = SSS
        self.SBP = SBP
        self.Mag = Mag
        self.PlanBlue = PlanBlue
        self.Camera = Camera
        self.OAS = OAS
        self.Speed = Speed
        self.Height = Height
        self.Acoms = Acoms
        self.InCurve = InCurve #bool
        self.type = 'GoTo'
        self.IsRunInRunOutPoint = IsRunInRunOutPoint #bool
        self.Name = Name

class Curve:
    def __init__(self,DestPoint,RotationPoint,MBES,SSS,SBP,Mag,PlanBlue,Camera,OAS,Speed,Height,Acoms,Direction):
        self.RotationPointX = RotationPoint.x()
        self.RotationPointY = RotationPoint.y()
        self.DestPointX = DestPoint.x()
        self.DestPointY = DestPoint.y()
        self.MBES = MBES
        self.SSS = SSS
        self.SBP = SBP
        self.Mag = Mag
        self.PlanBlue = PlanBlue
        self.Camera = Camera
        self.OAS = OAS
        self.Speed = Speed
        self.Height = Height
        self.Acoms = Acoms
        self.InCurve = True
        self.Direction = Direction
        self.type = 'Curve'


class Rows:
    def __init__(self,ListOfGotosOrCurves,Speed,MBES,SSS,SBP,Mag,PlanBlue,Camera,OAS,Height,Acoms,Name,InverseListOfGotosOrCurves):
        self.ListOfGoTosOrCurves = ListOfGotosOrCurves
        self.Speed = Speed
        self.MBES = MBES
        self.SSS = SSS
        self.SBP = SBP
        self.Mag = Mag
        self.PlanBlue = PlanBlue
        self.Camera = Camera
        self.Height = Height
        self.Acoms = Acoms
        self.OAS = OAS
        self.type = 'Rows'
        self.Name = Name
        self.InverseListOfGotosOrCurves = InverseListOfGotosOrCurves

class Line:
    def __init__(self,ListOfGotos,Speed,MBES,SSS,SBP,Mag,PlanBlue,Camera,OAS,Height,Acoms,Name):
        self.ListOfGoTosOrCurves = ListOfGotos
        self.Speed = Speed
        self.MBES = MBES
        self.SSS = SSS
        self.SBP = SBP
        self.Mag = Mag
        self.PlanBlue = PlanBlue
        self.Camera = Camera
        self.Height = Height
        self.Acoms = Acoms
        self.OAS = OAS
        self.type = 'Line'
        self.Name = Name

class LineWStops:
    def __init__(self,ListOfGotos,Speed,MBES,SSS,SBP,Mag,PlanBlue,Camera,OAS,Height,Acoms,Name, Duration,InverseListOfGotosOrCurves):
        self.ListOfGoTosOrCurves = ListOfGotos
        self.Speed = Speed
        self.MBES = MBES
        self.SSS = SSS
        self.SBP = SBP
        self.Mag = Mag
        self.PlanBlue = PlanBlue
        self.Camera = Camera
        self.Height = Height
        self.Acoms = Acoms
        self.OAS = OAS
        self.type = 'LineWStops'
        self.Name = Name
        self.Duration = Duration
        self.InverseListOfGotosOrCurves = InverseListOfGotosOrCurves

class Mission:
    def __init__(self,MissionCriticals,SafeAltitude,MissionEndBehavior,LowBatteryTreshold,ListOfManouvres):
        self.MissionCriticals = MissionCriticals
        self.SafeAltitude = SafeAltitude
        self.MissionEndBehavior = MissionEndBehavior
        self.LowBatteryTreshold = LowBatteryTreshold
        self.ListOfManouvres = ListOfManouvres