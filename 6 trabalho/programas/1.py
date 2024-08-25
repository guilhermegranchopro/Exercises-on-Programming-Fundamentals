# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 00:01:48 2022

@author: guilh
"""

from tkinter.filedialog import askopenfilename

def information():
    
    print('\n')
    print('Este programa calcula o consume médio de combustível de uma automóvel ao longo de vários trajetos e também na totalidade dos trajetos.\n')
    print('Deve agora selecionar um ficheiro do tipo txt que contenha o valor inicial e final do odómetro em Km, assim como o valor do combustível consumido em litros, de cada trajeto. Os valores devem ser escritos no ficheiro na ordem em que foram enunciados neste texto e para distinguir os valores dos diferentes trajetos escreva-os em linhas diferentes.\n')

def data():

    totalInformation = []
    
    fileName = askopenfilename()
    file = open(fileName, 'r')
    
    for line in file.readlines():
        information = []
        information = line.split(' ')
        information[0], information[1] = float(information[1]) - float(information[0]), float(information[2])
        information.pop(2)
        totalInformation.append(information)
       
    file.close()
      
    return(totalInformation)

def final(totalInformation):
    
    trajectory = []
    averageConsume = 0
    totalKm = 0
    totalAverageConsume = 0
    totalL = 0
    
    for a in range(len(totalInformation)):
       trajectory = totalInformation[a]
       averageConsume = 100 * trajectory[1] / trajectory[0]
       totalInformation[a] = averageConsume
       print('No trajeto', a+1, 'o automóvel consumiu em média', round(averageConsume, 3), 'litros de combustível por cada 100 Km.')
       totalKm = trajectory[0] + totalKm
       totalL = trajectory[1] + totalL
    
    totalAverageConsume = 100 * totalL / totalKm
    print('Na totalidade de todas as trajetórias o automóvel consumiu em média', round(totalAverageConsume, 3), 'litros de combustível por cada 100 Km.')

information()
final(data())