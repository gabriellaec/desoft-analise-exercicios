def segundostotal(dias, horas, minutos, segundos):
dias = int(input("Quantos dias?"))
horas = int(input ("Quantas horas?"))
minutos = int(input("Quantos minutos"))
segundos = int(input("Quantos segundos?"))
y = segundos + minutos*60 + horas*3600 + dias*86400
print (y)