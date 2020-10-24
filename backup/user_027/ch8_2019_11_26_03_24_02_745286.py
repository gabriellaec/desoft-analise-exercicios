# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 19:51:29 2019

Exercício 8: Progressão Aritmética e Progressão Geométrica
Escreva uma função que recebe uma lista de números e devolve "PA", se ela for 
uma progressão aritmética, "PG", se for uma progressão geométrica, e "NA" se não 
for nenhuma das duas. Caso a sequência seja tanto uma PA quanto uma PG, devolva "AG".
"""
def verifica_PA(x):
    x = [float(i) for i in x]
    razao = x[1] - x[0]
    for i in range(len(x)):
        if x[i] - x[i-1] != razao:
            return False
    return True

def verifica_PG(x):
    razão = x[1]/x[0]
    for i in range(len(x)):
        if x[i+1]/x[i] != razão:
            return False
    return True

def verifica_progressao(x):
    if verifica_PG(x) and verifica_PA(x):
        return "AG"
    elif verifica_PG(x):
        return 'PG'
    elif verifica_PA(x):
        return 'PA'
    else:
        return 'NA'
    
