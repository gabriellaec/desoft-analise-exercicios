# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:33:13 2019

@author: RafaelzZ
"""
def eh_bissexto(ano):
    if a%400 == 0:
        return True
    elif a%100 == 0:
        return False
    elif a%4 == 0:
        return True
    else:
        return False