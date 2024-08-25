# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 18:30:42 2022

@author: guilh
"""

from graphics import *
from Face import *

def main2():
    
    win = GraphWin("FACE", 700, 700)
    win.setCoords(0, 0, 100, 100)
    
    Smile = Face(win, Point(50,50), 10)
    trocarX, trocarY = 1, 1
    
    while True:
        trocarX, trocarY = Smile.moved(trocarX, trocarY)
        update(20)

main2()