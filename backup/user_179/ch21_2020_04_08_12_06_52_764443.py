dias = int(input('Quantos dias? '))
horas = int(input('Quantas horas? '))
minutos = int(input('Quantos minutos? '))
segundos = int(input('Quantos segundos?'))

ds = dias * 24 * 60 * 60
hs = horas * 60 * 60
ms = minutos * 60

total = ds + hs + ms + segundos
print(total)