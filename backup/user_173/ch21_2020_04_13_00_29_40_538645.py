d = int(input('Escreva quantos dias: '))
h = int(input('Escreva quantas horas: '))
m = int(input('Escreva quantos minutos: '))
s = int(input('Escreva quantos segundos: '))

s = 1*s
d = 86400*s
h = 3600*s
m = 60*s

total = d + h + m + s
print ('O total em segundos é {0}'.format(total))