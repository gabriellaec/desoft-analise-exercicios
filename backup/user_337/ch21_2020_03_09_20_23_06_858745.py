dias = int(input('Escreva uma quantidade de dias '))
horas = int(input('Escreva uma quantidade de horas '))
minutos = int(input('Escreva uma quantidade de minutos '))
segundos = int(input('Escreva uma quantidade de segundos '))
total = (dias * 86400) + (horas*3600) + (minutos*60) + segundos
print(total)