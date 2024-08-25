# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:10:14 2022

@author: guilh
"""

from graphics import *

win=GraphWin("FACE", 1500, 700)
win.setCoords(0.0, 0.0, 15.0, 7.0)

message = Text(Point(8, 0.5), "Click on two points to draw a face.")
message.draw(win)

p1=win.getMouse()
p1.draw(win)
p2=win.getMouse()
p2.draw(win)

face=Oval(p1,p2)
p1.undraw()
p2.undraw()
face.draw(win)

message.setText('Click on two points to draw an eye.')

p1=win.getMouse()
p1.draw(win)
p2=win.getMouse()
p2.draw(win)

raio=((((p1.getX()-p2.getX())**(2))+((p1.getY()-p2.getY())**2))**(0.5))

eye=Circle(p1,raio)
p1.undraw()
p2.undraw()
eye.setFill("black")
eye.draw(win)

message.setText('Repet to draw the last eye.')

p1=win.getMouse()
p1.draw(win)
p2=win.getMouse()
p2.draw(win)

raio=((((p1.getX()-p2.getX())**(2))+((p1.getY()-p2.getY())**2))**(0.5))

eye2=Circle(p1,raio)
p1.undraw()
p2.undraw()
eye2.setFill("black")
eye2.draw(win)

message.setText('Now you will draw the nose, click on three points.')

p1=win.getMouse()
p1.draw(win)
p2=win.getMouse()
p2.draw(win)
p3=win.getMouse()
p3.draw(win)

nose=Polygon(p1,p2,p3)
p1.undraw()
p2.undraw()
p3.undraw()
nose.setFill("black")
nose.draw(win)

message.setText('Now you will draw the mouth, click on two points.')

p1=win.getMouse()
p1.draw(win)
p2=win.getMouse()
p2.draw(win)

mouth=Line(p1,p2)
p1.undraw()
p2.undraw()
mouth.setOutline("red")
mouth.draw(win)

message.setText('Click anywhere to close the program.')
win.getMouse()
win.close()