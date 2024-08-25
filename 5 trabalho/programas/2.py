# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:22:25 2022

@author: guilh
"""

def bissexto(ano):
    
    valid=False
    
    if (ano%4==0 and ano%100==0 and ano%400==0) or (ano%4==0 and ano%100!=0): 
        valid = True
    
    return(valid)

def main():
    
    valid = False
    dateSTR=['0', '0', '0']
    dateINT=[0, 0, 0]
    
    dateSTR = input('Write here your date: ').split('/')
    
    for a in range(3):
        dateINT[a] = int(dateSTR[a])
         
    if 1<=dateINT[0]<=31 and 1<=dateINT[1]<=12 and 1<=dateINT[2]:
        valid = True
        if dateINT[0]==31 and (dateINT[1]==4 or dateINT[1]==6 or dateINT[1]==9 or dateINT[1]==11):
            valid = False
        if 29<dateINT[0] and dateINT[1]==2:
            valid = False
        if dateINT[0]==29 and bissexto(dateINT[2])==False and dateINT[1]==2:
            valid = False
            
    print()
    print(valid)
    
main()