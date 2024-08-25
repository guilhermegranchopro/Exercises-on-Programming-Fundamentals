# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 01:15:00 2022

@author: guilh
"""

from tkinter.filedialog import askopenfilename

def QuadradoElementos(numeros):
    
    for a in range(len(numeros)):
        b = (numeros[a])**2
        numeros[a] = b
    
    return(numeros)

def SomatorioLista(numeros):
    
    b=0
    
    for a in range(len(numeros)):
        b=b+(numeros[a])
        
    return(b)

def ConverteEmNumeros(ListaCaracteres):
    
    ListaCaracteres2 = (ListaCaracteres.split(" "))
    
    for a in range(len(ListaCaracteres2)):
        b = float(ListaCaracteres2[a])
        ListaCaracteres2[a] = b
        
    return(ListaCaracteres2)       

def main():
    
    a = 0
    
    fileName = askopenfilename()
    file = open(fileName, 'r')
    
    for line in file.readlines():
       a = a + SomatorioLista(QuadradoElementos(ConverteEmNumeros(line))) 
        
    file.close()
    
    return(a)
    
print(main())