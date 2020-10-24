#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:55:51 2019

@author: ellenbeatriz
"""

def libras_para_kg(x):
    kg = x/2.2046
    return '{0:.6f}'.format(kg) 
print (libras_para_kg(4))