import math

d = int (input('Quantos dias?:'))
h = int (input('Quantas horas?:'))
m = int (input('Quantos minutos?:'))
s = int (input('Quantos segundos?:'))

def calcula_segundo(d,h,m,s):
    T = (d * 24 * 3600) + (h*3600) + (m*60) + s
    return T

print(calcula_segundo(d,h,m,s))