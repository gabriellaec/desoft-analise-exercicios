import math

a = input('Ha quantos anos voce fuma?: ')
c = input('Quantos cigarros fumas por dia?: ')
a = float(a)
c =float(c)
def tempo_perdido_minutos(a,c):
    z = (a*365)*(c)*(10/1440)
    return z

print(tempo_perdido_minutos(a,c))