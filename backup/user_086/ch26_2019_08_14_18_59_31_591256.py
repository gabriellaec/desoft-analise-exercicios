dias=int(input('Digite uma quantidade de dias: '))
horas=int(input('Digite uma quantidade de horas '))
minutos=int(input('Digite uma quantidade de minutos: '))
segundos=dias*24*60*60+horas*60*60+minutos*60
print('A quantidade de tempo total equivalente ao tempo escolhido em segundos é {0}'.format(segundos))