dia = int(input("Entre com o dia: "))
horas = int(input("Entre com o horas: "))
minutos = int(input("Entre com o minutos: "))
segundos = int(input("Entre com o segundos: "))

seg = dia*24*60*60 + horas*60*60 + minutos*60 + segundos
print(seg)