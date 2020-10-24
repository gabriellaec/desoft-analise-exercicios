#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 13:55:51 2019

@author: ellenbeatriz
"""
def eh_primo(a):
    n = True
    d = 2
    while d<a:
        if a % d == 0:
            n = False
        d +=1
    return n

print(eh_primo(33))