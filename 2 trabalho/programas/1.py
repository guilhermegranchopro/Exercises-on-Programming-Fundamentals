# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:08:26 2022

@author: guilh
"""

def main():
    
    print()
    print()
    for celsius in range(0, 110, 10):   
       fahrenheit = 9/5 * celsius + 32
       print(celsius,'degrees celsius =', fahrenheit, 'degrees fahrenheit.')
       print()

main()