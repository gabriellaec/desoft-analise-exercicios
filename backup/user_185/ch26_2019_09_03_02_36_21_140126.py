dias = int(input("Digite o número de dias: "))

horas = int(input("Digite o número de horas: "))

minutos = int(input("Digite o número em minutos: "))

segundos = int(input("Digite o número em segundos: "))

tempo_segundos = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos

print(tempo_segundos)	