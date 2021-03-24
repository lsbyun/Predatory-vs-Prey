'''
Created on Dec 13, 2020

@author: Lawrence
'''
from blackhole import Black_Hole
from prey import Prey

#Special will boost the speed of any prey that goes in it but not for Hunters
#The speed will keep increasing if the prey goes into another Special simulton    
class Special(Black_Hole):
    def __init__(self, x, y):
        Black_Hole.__init__(self, x, y)
        
    def update(self, model):
        objects = model.find(lambda x : self.contains(x.get_location()))
        prey = set()
        for i in objects:
            if isinstance(i, Prey):
                prey.add(i)
        for i in prey:
            x = i.get_speed()
            newspeed = x + 5
            i.set_speed(newspeed)
            
    def display(self, canvas):
        canvas.create_oval(self._x-self.radius, self._y-self.radius, self._x+self.radius, self._y+self.radius, fill = 'green')
        
        
        
        
        