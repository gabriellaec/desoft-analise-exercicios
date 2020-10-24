d = input('Dias:')
h = input('Horas:')
m = input('Minutos:')
s = input('Segundos:')

def st(d,h,m,s):
    return (s+(60*m)+((60**2)*h)+(86400*d))
print (st)