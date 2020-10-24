def total_segundos(d,h,m,s):
    segundos = (d*24*60*60) + (h*60*60) + (m*60) + s
    return segundos
a = int(input('dias?')
b = int(input('horas?')
c = int(input('minutos?')
d = int(input('segundos?')
print ('o total de segundos é {0}.format(total_segundos(a,b,c,d))