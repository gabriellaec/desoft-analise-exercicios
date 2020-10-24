#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:26:51 2019

@author: ellenbeatriz
"""

def pos_arroba(x):
    arroba = '@'
    i = 0
    pos = -1
    while i < len(x):
        pos += 1
        if x[i] == arroba:
            return pos
        i += 1
        
        
print(pos_arroba("ellen@gmail.com"))
        