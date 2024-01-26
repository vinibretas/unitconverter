# Last modified: quinta 22/dec/2022 15:08:39

class IMarker:
    def __init__(self):
        self.imark_counter = 0
        self.MAPPING = {}
    def imark(self, reset = False):
        if reset: self.imark_counter = 0
        # retrieves current I counter
        result = self.imark_counter
        # increases counter in 1, so in next call, it gets
        # the increased value
        self.imark_counter += 1
        return result
    def __repr__(self):
        return str(self.imark_counter)

TYPE = IMarker()
temperature = TYPE.imark()
preassure = TYPE.imark()
volume = TYPE.imark()
nmols = TYPE.imark()
mass = TYPE.imark()
molmass = TYPE.imark()
speed = TYPE.imark()
energy = TYPE.imark()
time = TYPE.imark()
angle = TYPE.imark()
frequency = TYPE.imark()
lenght = TYPE.imark()
area = TYPE.imark()
force = TYPE.imark()
accel = TYPE.imark()
voltage = TYPE.imark()
current = TYPE.imark()
charge = TYPE.imark()

TYPE.MAPPING = {
    temperature : ("K", "C", "F","temperature"),
    preassure : ("Pa", "atm", "bar", "mmHg", "N/m2","preassure"),
    volume : ("m3", "L","mca","volume"),
    nmols : ("mol", "molar"),
    mass : ("g", "oz", "lb","ton", "mass"),
    molmass : ("g/mol", "molar mass"),
    speed : ("m/s", "km/h", "in/s", "ft/s","mi/h", "speed"),
    energy : ("J", "cal", "Btu", "energy"),
    time : ("s", "min","hr", "day","week","month","year", "time"),
    angle : ("°", "rad", "angle"),
    frequency : ("Hz", "/s", "frequency"),
    lenght : ("m", "mi","in","ft", "lenght"),
    area : ("m2", "mi2", "in2", "ft2", "area"),
    force : ("N", "kgf", "force"),
    accel : ("m/s2", "accel"),
    voltage : ("V", "voltade"),
    current : ("A", "current"),
        }

class Measurement:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self.type = None
        for k,v in TYPE.MAPPING.items():
            for m in v[:-1]:
                if self.unit.lower() == m.lower(): 
                    self.type = TYPE.MAPPING[k][-1]
                    self.unit = m
                    break
    
    def __repr__(self) -> str:
        return "{} {} ({})".format(self.value, self.unit,self.type.upper())

    def __str__(self):
        return "{} {}".format(self.value, self.unit,self.type.upper())


