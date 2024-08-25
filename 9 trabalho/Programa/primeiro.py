# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:51:12 2022

@author: guilh
"""

from graphics import *

def limites(X, Y, trocarX, trocarY):
    
    print(X, Y)
    
    if 5==X:
        trocarX = 1
    if 95==X:
        trocarX = -1
    if 5==Y:
        trocarY = 1
    if 95==Y:
        trocarY = -1

    return trocarX, trocarY

def iniciar():
    
    win = GraphWin("RESSALTO", 700, 700, autoflush=False)
    win.setCoords(0, 0, 100, 100)
    
    centro = Point(60,40)
    
    bola = Circle(centro, 5)
    bola.setFill('Red')
    bola.draw(win)
    
    return win, bola, centro

def movimento():
    
    win, bola, centro = iniciar()
    X = centro.getX()
    Y = centro.getY()
    trocarX, trocarY = 1, 1
    
    while True:
        trocarX, trocarY = limites(X, Y, trocarX, trocarY)
        bola.move(trocarX, trocarY)
        X = X + trocarX
        Y = Y + trocarY
        update(20) 
    
movimento() 