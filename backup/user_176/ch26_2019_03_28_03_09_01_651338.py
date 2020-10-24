d= int(input('quantidade de dias: '))
h= int(input('quantidade de horas: '))
m= int(input('quantidade de minutos: '))
s= int(input('quantidade de segundos: '))
total_segundos = s + m*60 + h*3600 + d*86400
print(total_segundos)