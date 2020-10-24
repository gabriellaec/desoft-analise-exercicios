import math
d = input('Dias:')
h = input('Horas:')
m = input('Minutos:')
s = input('Segundos:')

st = (s+(60*m)+((60**2)*h)+(86400*d))
print (st)