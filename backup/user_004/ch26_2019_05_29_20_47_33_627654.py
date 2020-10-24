dias=int(input('Quantos dias? '))
horas=int(input('Quantas horas? '))
minutos=int(input('Quantos minutos? '))
segundos=int(input('Quantos segundos? '))

segundosDias=dias*86400
segundosHoras=horas*3600
segundosMinutos=minutos*60

total=segundosDias+segundosHoras+segundosMinutos+segundos

print(total)