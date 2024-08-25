# -*- coding: utf-8 -*-
"""
Created on Tue May 17 20:43:21 2022

@author: guilh
"""

from GrupoGrafico import *
from graphics import *

def facef(C, face):
    
    obejeto0 = Circle(C, 20)
    face.AdicionaObjeto(obejeto0)
    objeto1 = Line(Point(C.getX()-5, C.getY()-10), Point(C.getX()+5, C.getY()-10))
    face.AdicionaObjeto(objeto1)
    objeto2 = Circle(Point(C.getX()-5, C.getY()+10), 5)
    face.AdicionaObjeto(objeto2)
    objeto3 = Circle(Point(C.getX()+5, C.getY()+10), 5)
    face.AdicionaObjeto(objeto3)

def main():
    
    valid = True
    
    win = GraphWin("FACE", 600, 600)
    win.setCoords(0, 0, 100, 100)
    
    message = Text(Point(50, 10), "Click where you want the face!")
    message.draw(win)
    
    face = GrupoGrafico(win.getMouse())
    C = face.retornaAncora()
    
    facef(C, face)
    
    face.desenha(win)
    
    while valid == True:
        D = win.getMouse()
        face.apaga()
        face.move(D.getX(), D.getY())
        C = face.retornaAncora()
        facef(C, face)
        face.desenha(win)

main()