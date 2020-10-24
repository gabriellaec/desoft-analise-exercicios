dias = int(input('Dias? '))
horas = int(input('Horas? '))
minutos = int(input('Minutos? '))
segundos = int(input('Segundos? '))

total_segundos = dias*24*60*60 + horas*60*60 + minutos*60 + segundos

print(total_segundos)