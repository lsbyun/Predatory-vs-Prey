# The Hunter class is derived from Pulsator (1st) and the Mobile_Simulton (2nd).
#   It updates/displays like its Pulsator base, but also moves (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey  import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton): 
    distantc = 200
    def __init__(self, x, y):
        Mobile_Simulton.__init__(self, x, y, 20, 20, 0, 5)
        Pulsator.__init__(self, x, y)
        self.randomize_angle()
    
    def update(self, model):
        updated = Pulsator.update(self, model)
        objects = model.find(lambda x : self.distance(x.get_location()) <= 200)
        prey = set()
        for i in objects:
            if isinstance(i, Prey):
                prey.add(i)
        if len(prey) != 0:
            lst = []
            for i in prey:
                lst.append(self.distance(i.get_location()))
            closestdist = min(lst)
            for i in prey:
                if self.distance(i.get_location()) == closestdist:
                    closestprey = i
            x,y = closestprey.get_location()
            angle = atan2(y - self._y, x - self._x)
            self.set_angle(angle)
        self.move()
        return updated