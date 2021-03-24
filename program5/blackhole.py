# The Black_Hole class is derived from Simulton. It updates by finding/removing
#   any class derived from Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton): 
    radius = 10
    def __init__(self, x, y):
        Simulton.__init__(self, x, y, 20, 20)
    
    def update(self, model):
        objects = model.find(lambda x : self.contains(x.get_location()))
        prey = set()
        for i in objects:
            if isinstance(i, Prey):
                prey.add(i)
        for i in prey:
            model.remove(i)
        return prey
    
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius, self._y-self.radius, self._x+self.radius, self._y+self.radius, fill = 'black')
    
    def contains(self, xy):
        x = self.distance(xy)
        return x < self.radius
