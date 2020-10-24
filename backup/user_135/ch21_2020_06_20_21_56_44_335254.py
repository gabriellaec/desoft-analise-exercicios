dias = int(input())
horas = int(input())
minutos = int(input())
segundos = int(input())

total_segundos = segundos + minutos*60 + horas*60*60 + dias*24*60*60
print(total_segundos)