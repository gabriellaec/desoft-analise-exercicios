dia=int(input('Dia: '))
hora= int(input('Hora: '))
minuto= int(input('Minuto: '))
segundo= int(input('segundo: '))
dia_em_segundo=dia*86400
hora_em_segundo=hora*3600
minuto_em_segundo=minuto*60
quantos_segundos=dia_em_segundo+hora_em_segundo+minuto_em_segundo+segundo
print(quantos_segundos)