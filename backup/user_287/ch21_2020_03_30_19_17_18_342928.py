d = int(input('dias:'))
h = int(input('horas'))
m = int(input('minutos:'))
s = int(input('segundos:'))
total = m*60 + h*3600 + d*86400 + s
print('segundos:',total)