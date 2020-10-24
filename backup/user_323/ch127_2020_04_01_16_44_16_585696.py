import math
def calcula_elongacao(A,fi,omega,t):
    x=A*(math.cos(fi)+omega*t)
    return x
