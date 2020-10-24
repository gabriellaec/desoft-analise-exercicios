dias = input(float('Insira a quantidada de dias: '))
horas = input(float('Insira a quantidade de horas: '))
minutos = input(float('Insira a quantidade de minutos: '))
segundos = input(float('Insira a quantidade de segundos: '))

total = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos  
print(total)