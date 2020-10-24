a= int(input('diga uma quantidade de dias: '))
b= int(input('diga uma quantidade de horas: '))
c= int(input('diga uma quantidade de minutos:'))
d= int(input('diga uma quantidade de segundos: '))
total= d+ c*60 + b*360 + a*86400
print(total)       