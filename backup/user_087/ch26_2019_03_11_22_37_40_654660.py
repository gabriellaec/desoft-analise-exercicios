def total_segundos(d,h,m,s):
    segundos = (d*24*60*60) + (h*60*60) + (m*60) + s
    return segundos
d = int(input('dias?')
h = int(input('horas?')
m = int(input('minutos?')
s = int(input('segundos?')
print (total_segundos(d,h,m,s))