número_cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos_fumando = int(input("Quantos anos você fuma? "))
tempo_perdido = número_cigarros * 1/144 * anos_fumando * 1/365
print(tempo_perdido)
