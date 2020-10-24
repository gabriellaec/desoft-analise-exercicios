dias = int(input('dias:'))
horas = int(input('horas:'))
minutos = int(input('minutos:'))
segundos = int(input('segundos:'))

total_segundos = (dias*24*60*60)+(horas*60*60)+(minutos*60)+segundos

print(total_segundos)