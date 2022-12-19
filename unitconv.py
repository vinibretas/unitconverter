
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
    temperature : (("K","Kelvin"),("C", "Celcius"),("F","Fahrenheit")),
    preassure : [],
    volume : [],
    nmols : [],
    mass : [],
    molmass : [],
    speed : [],
    energy : [],
    time : [],
    angle : [],
    frequency : [],
    lenght : [],
    area : [],
    force : [],
    accel : [],
    voltage : [],
    current : [],
    charge : []
        }

class Measurement:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
        self.type = None

print(TYPE.MAPPING[temperature])
