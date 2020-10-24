'''funcao que calcula a posicao (x) de uma partícula em movimento harmonico simples (MHS)
em um instante de tempo (t)
'''
import math
def calcula_elongacao(A,teta0,omega,t):
    x = A
    y = math.cos((math.radians(teta0))+(omega)*t)
    w = math.radians(y)
    z = x * w
    return z