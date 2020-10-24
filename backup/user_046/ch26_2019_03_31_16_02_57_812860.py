dias=input(int("Quantos dias? ")
horas=input(int("Quantas horas? "))
minutos=input(int("Quantos minutos? "))
segundos=input(int("Quantos segundos? "))
t=dias*24
u=horas+t*60
y=u+minutos*60
total=t+u+y
print(total)
