# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 14:14:42 2022

@author: guilh
"""

from random import random

def information():
    
    print('\n')
    print('Este programa simula um jogo de volei entre as equipas A e B. Clique ENTER para continuar...')


def points(special, setsA, setsB):

    pointsA, pointsB, p = 0, 0, 0
    A = True
    
    while not((pointsA>=25 or pointsB>=25) and abs(pointsA - pointsB) >= 2):
        if random()<0.5:
            pointsA = pointsA + 1
        else:
            pointsB = pointsB + 1
        if special==True and setsA == 4 and pointsA>=15 and pointsA - pointsB >= 2:
            break
        elif special==True and setsB == 4 and pointsB>=15 and pointsB - pointsA >= 2:
            break
        
    if pointsA>pointsB:
        A = True
    else:
        A = False
        
    return(A, pointsA, pointsB)

def sets():
    
    setsA, setsB, pointsA, pointsB = 0, 0, 0, 0
    victoryA, special = True, False
    
    while setsA<5 and setsB<5:
        A, pointsA, pointsB = points(special, setsA, setsB)
        print('Pontuação do set:(A:B)',pointsA ,':' , pointsB)
        if A == True:
            setsA = setsA + 1
        else:
            setsB = setsB + 1
        print('Sets:(A:B)', setsA, ':', setsB,'\n')
        if setsA==2 and setsB==2:
            special = True

    if setsA == 5:
        victoryA = True
    else:
        victoryA = False
    
    return(victoryA)

def score(victoryA):
    
    if victoryA == True:
        print('A equipa A Venceu!')
    else:
        print('A equipa B Venceu!')

information()
input()
score(sets())
    