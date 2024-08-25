# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 20:22:55 2022

@author: guilh
"""

from tkinter.filedialog import askopenfilename

def data():

    totalInformation = []
    
    fileName = askopenfilename()
    file = open(fileName, 'r', encoding="utf8")
    
    for line in file.readlines():
        information = []
        information = line.split(' ; ')
        totalInformation.append(information)
       
    file.close()
      
    return(totalInformation)

def ordemDosAutores(totalInformation):
    
    autores = []
    listaDeAutores = []

    for a in range(length(totalInformation)):
        autores = totalInformation[a][1]
        listaDeAutores.append(autores)
    
    listaDeAutores.sort()
    print(listaDeAutores)
    
ordemDosAutores(data())