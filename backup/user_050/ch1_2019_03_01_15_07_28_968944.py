"""
Exercício 1: Cálculo de Juros Compostos

Variáveis:
    V = valor devido
    C = capital inicial(Valor emprestado)
    i = taxa de juros
    t= período de tempo
    
"""

def calcula_valor_devido(C,i,t):
    V = C*((1+i)**t)
    return V

