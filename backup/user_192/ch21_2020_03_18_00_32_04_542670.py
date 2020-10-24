dias = input('Quantos dias? ')
horas = input('Quantas horas? ') 
minutos = input('Quantos minutos? ') 
segundos = input('Quantos segundos? ')

total_segundos = (dias*86400) + (horas*3600) + (minutos*60) + segundos

print(total_segundos)