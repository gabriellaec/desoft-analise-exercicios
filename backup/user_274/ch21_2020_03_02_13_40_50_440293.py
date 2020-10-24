dias = int(input("Escolha uma quantidade de dias. "))
horas = int(input("Escolha uma quantidade de horas. "))
minutos = int(input("Escolha uma quantidade de minutos. "))
segundos = int(input("Escolha uma quantidade de segundos. "))

total = dias*86400 + horas*3600 + minutos*60 + segundos

print(total)