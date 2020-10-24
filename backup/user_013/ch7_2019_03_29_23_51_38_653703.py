import math
def calcula_norma(v):
    #índice i
    i = 0
    #Resultado do quadrado da Norma, N2
    N2 = 0
    #Looping para recebimento de valores em N2
    while i <= len(v)-1:
        N2 += v[i]**2
        i += 1
    return math.sqrt(N2)