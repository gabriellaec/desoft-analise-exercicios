dias = int(input("Quantos dias?"))
horas = int(input("Quantas horas?"))
minutos = int(input("Quantos minutos?"))
segundos = int(input("Quantos segundos?"))

total = segundos + minutos*60 + horas *3600 + dias *24*3600
print(total)
