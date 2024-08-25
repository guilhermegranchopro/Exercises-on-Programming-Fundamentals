# -*- coding: utf-8 -*-
"""
Created on Sat Apr  2 14:34:51 2022

@author: guilh
"""

from graphics import *

win=GraphWin("Draw a Rectangle", 1500, 700)
win.setCoords(0.0, 0.0, 15.0, 7.0)

message = Text(Point(8, 0.5), "Click on two points, to draw a rectangle.")
message.draw(win)

p1=win.getMouse()
p1.draw(win)
p2=win.getMouse()
p2.draw(win)

rect=Rectangle(p1, p2)
rect.setFill("red")
rect.setOutline("red")
p1.undraw()
p2.undraw()
rect.draw(win)

A=(abs((p1.getX()-p2.getX())*(p1.getY()-p2.getY())))
P=(abs(p1.getX()-p2.getX())*2 + abs(p1.getY()-p2.getY())*2)

perimeterMessage=('The perimeter of the rectangle is ' + str(round(P, 2)) + '.')
areaMessage=('The area of the rectangle is ' + str(round(A, 2)) + '.')

message.setText(perimeterMessage)
win.getMouse()
message.setText(areaMessage)
win.getMouse()

message.setText('Click anywhere to close the program.')
win.getMouse()
win.close()