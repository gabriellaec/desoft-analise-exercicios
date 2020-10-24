dias= int(input("Quantos dias? "))
horas= int(input("Quantos horas? "))
minutos= int(input("Quantos minutos? "))
total_segundos= minutos*60 + horas*60*60 + dias*60*60*24
print(total_segundos)