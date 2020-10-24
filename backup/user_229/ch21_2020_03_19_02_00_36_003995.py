dias = int(input("Quantos dias? "))
horas = int(input("Quantas horas? "))
minutos = int(input("Quantos minutos? "))
segundos = int(input("Quantos segundos? "))
def total(segundos, minutos, horas, dias):
    y = segundos+(minutos*60)+(3600*horas)+(dias*24*3600)
    return y
print(total)