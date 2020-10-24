dias= int(input("Quantos dias? "))
horas= int(input("Quantos horas? "))
minutos= int(input("Quantos minutos? "))
segundos= int(input("Quantos segundos? "))
total_segundos= minutos*60 + horas*60*60 + dias*60*60*24 + segundos
print(total_segundos)