"""
Exercício 1: Cálculo de Juros Compostos

Variáveis:
    V = valor emprestado
    C = capital inicial(Valor emprestado)
    i = taxa de juros
    t= período de tempo
    
"""

def calcula_valor_devido(C,t,i):
    V = C*((1+i)**t)
    return V

