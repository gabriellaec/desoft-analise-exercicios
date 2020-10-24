dias = int(input("quantos dias"))
horas = int(input("quantas horas"))
minutos = int(input("quantas minutos"))
segundos = int(input("quantos segundos"))
dias2 = dias*86400
horas2 = horas*3600
minutos2 = minutos*60
tsegundos = dias2 + horas2 + minutos2 + segundos 
print(tsegundos)              