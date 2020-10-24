dias=int(input("Quantos dias? "))
horas=int(input("Quantas horas? "))
minutos=int(input("Quantos minutos? "))
segundos=int(input("Quantos segundos? "))

a=dias*86400
b=horas*3600
c=minutos*60
d=segundos
total = a+b+c+d
print(total)