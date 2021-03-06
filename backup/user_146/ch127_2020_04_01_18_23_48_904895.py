'''funcao que calcula a posicao (x) de uma partícula em movimento harmonico simples (MHS)
em um instante de tempo (t). A fórmula é x=A*cos(teta0+w*t)
'''
import math
def calcula_elongacao(A,phi0,omega,t):
    x = A
    y = math.cos((math.degrees(phi0))+(math.degrees(omega))*t)
    w = math.degrees(y)
    z = x * w
    return z
print(calcula_elongacao(10,20,30,40))