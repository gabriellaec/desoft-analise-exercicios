dias = int(input('Quantos dias? '))
horas = int(input('Quantas horas? '))
minutos = int(input('Quantos minutos? '))
segundos = int(input('Quantos segundos? '))

somadias = dias*86400
somahoras = horas*3600
somaminutos = minuts*60

somatotal = somadias + somahoras + somaminutos + segundos
print(somatotal)