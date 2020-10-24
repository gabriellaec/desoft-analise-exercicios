dias=int(input('Quantos dias? '))
horas=int(input('Quantas horas? '))
segundos=int(input('Quantos segundos? '))

segundosDias=dias*86400
segundosHoras=horas*3600

total=segundosDias+segundosHoras+segundos

print(total)