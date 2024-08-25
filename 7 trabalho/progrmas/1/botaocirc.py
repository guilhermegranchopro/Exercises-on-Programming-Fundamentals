# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:03:46 2022

@author: guilh
"""

from graphics import *

class BotaoCircular:

    def __init__(self, win, center, radius, label): 
        
        self.centerX = center.getX()
        self.centerY = center.getY()
        self.radius = radius
        self.cir = Circle(center, radius)
        self.cir.setFill('lightgray')
        self.cir.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "Returns true if button active and p is inside"
        return (self.active and abs(p.getX() - self.centerX) <= self.radius and abs(p.getY() - self.centerY) <= self.radius)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill('black')
        self.cir.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill('darkgrey')
        self.cir.setWidth(1)
        self.active = False