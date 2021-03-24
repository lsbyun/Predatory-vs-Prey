# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random


class Floater(Prey): 
    radius = 5
    def __init__(self,x,y):
        Prey.__init__(self,x,y, 10, 10, 0, 5)
        self.randomize_angle()
        self._image = PhotoImage(file = 'ufo.gif')
    
    def update(self, model):
        if random() < 1:
            x = self.get_speed() + (random() - 0.5)
            if x < 3:
                x = 3
            if x > 7:
                x = 7
            self.set_speed(x)
            self.set_angle(self.get_angle() + (random() - 0.5))
        self.move()
    
    def display(self, the_canvas):
        the_canvas.create_image(*self.get_location(), image = self._image)
