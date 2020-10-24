"""
Exercício 1: Cálculo de Juros Compostos

Variáveis:
    V = valor devido
    C = capital inicial (Valor emprestado)(n1)
    i = taxa de juros (n2)
    t= período de tempo (n3)
    
"""

def Calcula_Valor_Devido(n1,n2,n3):
    V = n1*(1+n2/100)**n3
    return V;