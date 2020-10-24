dias = int(input('Quantos dias? '))
horas = int(input('Quantas horas? '))
minutos = int(input('Quantos minutos? '))
segundos = int(input('Quantos segundos?'))

dias_para_segundos = dias * 24 * 60 * 60
horas_para_segundos = horas * 60 * 60
minutos_para_segundos = minutos * 60

total = dias_para_segundos + horas_para_segundos + minutos_para_segundos + segundos