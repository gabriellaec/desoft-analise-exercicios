dias = int(input('informe a quantidade de dias: ')) * 86400
horas = int(input('informe a quantidade de horas: ')) * 3600
minutos = int(input('informe a quantidade de minutos: ')) * 60
segundos = int(input('informe a quantidade de segundos: '))

soma_de_segundos = dias + horas + minutos + segundos
print('este é o tempo total em segundos = {}'.format(soma_de_segundos))
