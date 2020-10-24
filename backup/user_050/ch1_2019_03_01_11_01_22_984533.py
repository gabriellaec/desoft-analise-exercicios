"""
Exercício 1: Cálculo de Juros Compostos

Variáveis:
    V = valor devido
    C = capital inicial (Valor emprestado)(n1)
    i = taxa de juros (n2)
    t= período de tempo (n3)
    
"""

def calcula_valor_devido(C,i,t):
    V = C*(1+i/100**t)
    return V;

