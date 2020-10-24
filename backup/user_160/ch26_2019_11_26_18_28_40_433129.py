dias = input('Qual a quantidade de dias?')
horas = input('Qual a quantidade de horas?')
minutos = input('Qual a quantidade de minutos?')
segundos = input('Qual a quantidade de segundos?')

total = segundos + minutos*60 + horas*3600 + dias*3600*24
print(total)