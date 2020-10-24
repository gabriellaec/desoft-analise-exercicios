# -*- coding: utf-8 -*-
"""
programa que calcula a quantidade em segundos pelo input do usuário

@author: Francisco Janela
"""
#função para calcular o total em segundos
def calcula_segundos(d,h,m,s):
    dias=24*3600*d
    horas=3600*h
    minutos=60*s
    seg=dias+horas+minutos+s
    return seg

#define os inputs do usuário
dias=input('quantos dias? ')
horas=input('quantas horas? ')
minutos=input('quantos minutos? ')
segundos=input('quantos segundos? ')

print('total em segundos é: {0}'.format(calcula_segundos(int(dias),int(horas),int(minutos),int(segundos))))
