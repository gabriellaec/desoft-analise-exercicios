def st(d,h,m,s):
    return (s+(60*m)+((60**2)*h)+(86400*d))

d = int (input('Dias:'))
h = int (input('Horas:'))
m = int (input('Minutos:'))
s = int (input('Segundos:'))

print (st)