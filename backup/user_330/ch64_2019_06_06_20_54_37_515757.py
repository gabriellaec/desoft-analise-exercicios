#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:27:30 2019

@author: ellenbeatriz
"""

def pos_arroba(email):
    arroba ='@'
    i = 0
    pos = -1
    
    while i<len(email):
        pos+=1
        if email[i] == arroba:
            return pos
        i+=1   


def usuario(email):
    pos = pos_arroba(email)
    return email[:pos]

    
    