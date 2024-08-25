# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 18:21:58 2022

@author: guilh
"""

print()
print()
print()
print('--------Café e Bolos--------')
print()
print()

kilos=eval(input('How many kilos of coffee would you like to order? '))

print()

cost=(2.5+0.86)*kilos+1.5

print('Your order will cost', round(cost//1 + (cost%1) * 10, 2),'\N{euro sign}.')