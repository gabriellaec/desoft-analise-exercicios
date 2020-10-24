import math

a = input('Ha quantos anos voce fuma?: ')
c = input('Quantos cigarros fumas por dia?: ')
a = float(a)
c =float(c)
def tempo_perdido_minutos(a,c):
    z = (a)*(c)*0.006944
    return z

print(tempo_perdido_minutos(a,c))