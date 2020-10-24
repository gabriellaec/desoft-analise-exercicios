dias = input("Quantos dias?")
horas = input("Quantas horas?")
minutos = input("Quantos minutos?")
segundos = input("Quantos segundos?")

total = segundos + minutos*60 + horas *3600 + dias *24*3600
print(total)
