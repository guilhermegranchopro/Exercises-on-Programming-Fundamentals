# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 17:21:16 2022

@author: guilh
"""

# File: c01ex5.py 
# Chaos program that prints a variable number of terms 

def main(): 
    
    print()
    print()
    print("This program illustrates a chaotic function")
    
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? ")) 
    
    for i in range(n): 
        
        print()
        x = 3.9 * x * (1 - x)
        print(x)
        
main()
