d = int(input('Quantos dias? '))
h = int(input('Quantas horas? '))
m = int(input('Quantos minutos? '))
s = int(input('Quantos segundos? '))
total_segundos = 86400*d + 3600*h + 60*m + s
print ('O total de segundos e {0}'. format (total_segundos))