dias = int(input("Me fale quantos dias: "))
horas = int(input("Me fale quantos horas: "))
minutos = int(input("Me fale quantos minutos: "))
segundos = int(input("Me fale quantos segundos: "))
total = (dias*86400) + (horas*3600) + (minutos*60) + segundos
print(total)