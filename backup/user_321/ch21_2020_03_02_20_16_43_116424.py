d = int (input('Dias:'))
h = int (input('Horas:'))
m = int (input('Minutos:'))
s = int (input('Segundos:'))

st = (s+(60*m)+((60**2)*h)+(86400*d))
print (st)