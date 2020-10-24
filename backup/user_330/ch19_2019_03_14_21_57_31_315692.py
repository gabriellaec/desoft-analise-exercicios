#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:39:43 2019

@author: ellenbeatriz
"""
import math

def calcula_distancia_do_projetil(v, x, y0 ):
    g = 9.8
    d = ( (v**2) / 2*g ) * (1 + math.sqrt(1 + ((2 * g * y0) / ((v**2) * (math.sin(x))**2)))) * (math.sin(2*x))
    return d