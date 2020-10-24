d = int(input("dias: "))
h = int(input("horas: "))
m = int(input("minutos: "))
s = int(input("segundos: "))

minutos = m * 60
horas = h*3600
dias = d*3600*24

print(minutos + horas + dias + s) 