Dias= int(input('Diga uma quantidade de dias:'))
horas= int(input("Diga uma quantidade de horas: "))
minutos=int(input ("Diga uma quantidade de minutos:"))
segundos=int(input("Diga uma quantidade de segundos"))

total = segundos+(minutos*60)+(horas*3600)+(Dias*86400)

print(total)