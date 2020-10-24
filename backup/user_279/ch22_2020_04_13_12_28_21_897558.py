n_de_cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("A quantos anos você fuma? "))
Tempo_perdido = ((n_de_cigarros * 10) * anos) / 1440
print("você perdeu {} dias da sua vida",format(Tempo_perdido))