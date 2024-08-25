# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 10:16:18 2022

@author: guilh
"""

def wordCounter():

    counter=0
    
    print()
    print()
    print()
    print('---------Count the words in a text---------')
    print()
    print()

    print('Enter here your text:')
    text=str(input())

    for a in text.split():
        counter=counter+1
    
    print()
    print('Your text has', counter, 'words.')
    
wordCounter()
        