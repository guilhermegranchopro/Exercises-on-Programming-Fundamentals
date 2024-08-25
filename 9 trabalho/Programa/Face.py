# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 18:29:19 2022

@author: guilh
"""

# face.py 
from graphics import *

def limites(X, Y, trocarX, trocarY):
    print(X, Y)

    if 10 == X:
        trocarX = 1
    if 90 == X:
        trocarX = -1
    if 10 == Y:
        trocarY = 1
    if 90 == Y:
        trocarY = -1

    return trocarX, trocarY

class Face:

    def __init__(self, window, center, size):
        eyeSize = 0.15 * size
        eyeOff = size / 3.0
        mouthSize = 0.8 * size
        mouthOff = size / 2.0
        self.head = Circle(center, size)
        self.head.draw(window)
        self.leftEye = Circle(center, eyeSize)
        self.leftEye.move(-eyeOff, -eyeOff)
        self.rightEye = Circle(center, eyeSize)
        self.rightEye.move(eyeOff, -eyeOff)
        self.leftEye.draw(window)
        self.rightEye.draw(window)
        p1 = center.clone()
        p1.move(-mouthSize / 2, mouthOff)
        p2 = center.clone()
        p2.move(mouthSize / 2, mouthOff)
        self.mouth = Line(p1, p2)
        self.mouth.draw(window)
        self.center = center

    def moved(self, trocarX, trocarY):

        X = self.center.getX()
        Y = self.center.getY()

        trocarX, trocarY = limites(X, Y, trocarX, trocarY)
        self.head.move(trocarX, trocarY)
        self.leftEye.move(trocarX, trocarY)
        self.rightEye.move(trocarX, trocarY)
        self.mouth.move(trocarX, trocarY)
        X = X + trocarX
        Y = Y + trocarY
        self.center = Point(X, Y)

        return trocarX, trocarY