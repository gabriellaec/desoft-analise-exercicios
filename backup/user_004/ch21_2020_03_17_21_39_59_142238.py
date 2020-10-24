dias = int(input("Dias: "))
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))
segundos = int(input("Segundos: "))

diasToSec = dias/86400
horasToSec = horas/3600
minutosToSec = minutos/60

total = segundos + diasToSec + horasToSec + minutosToSec
print(total)