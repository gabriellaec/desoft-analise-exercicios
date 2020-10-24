dias = int(input("Número de dias: "))
horas = int(input("Número de horas: "))
minutos = int(input("Número de minutos: "))
segundos = int(input("Número de segundos: "))
total_segundos = (dias*86400)+(horas*3600)+(minutos*60)+segundos
print(total_segundos)