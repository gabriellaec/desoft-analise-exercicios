dias = int(input('informe a quantidade de dias: ')) * 21600
horas = int(input('informe a quantidade de horas: ')) * 360
minutos = int(input('informe a quantidade de minutos: ')) * 60
segundos = int(input('informe a quantidade de segundos: '))

soma_de_segundos = horas + minutos + segundos
print('este é o tempo total em segundos = {}'.format(soma_de_segundos))
