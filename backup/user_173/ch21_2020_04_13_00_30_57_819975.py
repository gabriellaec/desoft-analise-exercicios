d = int(input('Escreva quantos dias: '))
h = int(input('Escreva quantas horas: '))
m = int(input('Escreva quantos minutos: '))
s = int(input('Escreva quantos segundos: '))

segundos = 1*s
dias = 86400*s
horas = 3600*s
minutos = 60*s

total = dias + horas + minutos + segundos
print ('O total em segundos é {0}'.format(total))