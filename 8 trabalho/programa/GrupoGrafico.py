# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:01:16 2022

@author: guilh
"""

from graphics import *

class GrupoGrafico:
    
    def __init__(self, ancora):
        self.ancora = ancora
        self.objeto = []

    def retornaAncora(self):
        return(self.ancora)
        
    def AdicionaObjeto(self,objeto):
        self.objeto.append(objeto)

    def move(self,dx,dy):
        self.ancora = Point(dx, dy)
        
    def desenha(self, win):
        for a in range(len(self.objeto)):
            self.objeto[a].draw(win)
        
    def apaga(self):
        for a in range(len(self.objeto)):
            self.objeto[a].undraw()
        self.objeto = []