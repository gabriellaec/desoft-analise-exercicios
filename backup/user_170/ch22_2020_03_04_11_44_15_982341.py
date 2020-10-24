import math

a = input('Ha quantos anos voce fuma?: ')
c = input('Quantos cigarros fumas por dia?: ')
a = float(a)
c =float(c)
def tempo_perdido_minutos(a,c):
    z = (a)*(c)*10
    return z

x = tempo_perdido_minutos(a,c)
#converter minutos em dias
def converter(x):
    z = x*0.0069444
    return z

print(converter(x))