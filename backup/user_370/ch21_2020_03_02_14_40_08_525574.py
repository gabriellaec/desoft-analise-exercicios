dias=int(input('Quantidade de dias:'))
horas=int(input('Quantidade de horas: '))
minutos=int(input('Quantidade de minutos: '))
segundos=int(input('Quantidade de segundos: '))

total_segundos= (dias*86400)+(horas*3600)+(minutos*60)+segundos

print('O total sao {0} segundos'.format(total_segundos))
