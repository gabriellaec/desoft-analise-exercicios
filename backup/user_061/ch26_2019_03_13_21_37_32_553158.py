dias = int(input("DIAS"))
horas = int(input("HORAS"))
minutos = int(input("MINUTOS"))
segundos = int(input("SEGUNDOS"))

dias = dias*24*60*60
horas = horas*60*60
minutos = minutos*60
a = dias + horas + minutos + segundos 
print(a)

