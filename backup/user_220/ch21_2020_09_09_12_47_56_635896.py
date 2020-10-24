quantidade_dias = int(input('Quantos dias? '))
quantidade_horas = int(input('Quantas horas? '))
quantidade_minutos = int(input('Quantos minutos? '))
quantidade_segundos = int(input('Quantos segundos? '))
dias_em_segundos=quantidade_dias*86400
horas_em_segundos=quantidade_horas*3600
minutos_em_segundos=quantidade_minutos*60
print(quantidade_segundos+dias_em_segundos+horas_em_segundos+minutos_em_segundos)