#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:18:03 2019

@author: ellenbeatriz
"""

def celsius_para_fahrenheit(graus_c):
    graus_f = graus_c*(9/5) + 32
    return graus_f

#quanto é 0c em f?
celsius = 0
fahrenheit = celsius_para_fahrenheit (celsius)
print("{0} graus celsius são {1} graus fahrenheit" .format(celsius, fahrenheit))
