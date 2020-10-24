d = int(input('Escreva quantos dias: '))
h = int(input('Escreva quantas horas: '))
m = int(input('Escreva quantos minutos: '))
s = int(input('Escreva quantos segundos: '))

segundos = 1*s
dias = 86400*d
horas = 3600*h
minutos = 60*m

total = dias + horas + minutos + segundos
print ('O total em segundos é {0}'.format(total))