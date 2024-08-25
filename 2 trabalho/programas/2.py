# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:18:22 2022

@author: guilh
"""


def main():
    
    print()
    print()
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years of the investment: "))
    print()
    print()

    for i in range(years):
        principal = principal * (1 + apr)

    print('The value in', years, 'years is:', round(principal, 3))

main()