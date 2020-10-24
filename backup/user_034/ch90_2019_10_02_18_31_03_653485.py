# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 13:34:30 2019

@author: enzos
Questao 1 - P.I.
""" 
def segundos_entre(horario1,horario2):
    horario1=("10:10:10")
    horario2=("10:10:09")
    horas1=horario1[:3]
    horas2=horario2[:3]
    mins1=horario1[4:6]
    mins2=horario2[4:6]
    seg1=horario1[7:]
    seg2=horario2[7:]
    total1=(horas1*3600)+(mins1*60)+seg1
    total2=(horas2*3600)+(mins2*60)+seg2
    tudo=total1-total2
    return tudo
print(segundos_entre)
    