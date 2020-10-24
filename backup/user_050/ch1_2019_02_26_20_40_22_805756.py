# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 09:28:16 2019
Desafios resolvidos (ou não)
@author: Giovanni Rozatti
"""
"""
Exercício 1: Cálculo de Juros Compostos

Variáveis:
    V = valor devido
    C = capital inicial (Valor emprestado)
    i = taxa de juros
    t= período de tempo
    
"""

def Calcula_Valor_Devido(n1,n2,n3):
    V = n1*(1+n2/100)**n3
    return V;

c = int (input("digite o valor emprestado: "))
i = int (input("digite a taxa de juros ao mês: "))
t = int (input("digite o número de meses que se passaram desde o empréstimo: "))
V = Calcula_Valor_Devido(c,i,t)

print(V)