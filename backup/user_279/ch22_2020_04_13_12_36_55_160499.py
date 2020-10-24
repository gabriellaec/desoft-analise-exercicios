n_de_cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("A quantos anos você fuma? "))
cigarros = ((n_de_cigarros*365 )* anos)
Tempo_perdido = (cigarros * 10) / 1440
print("você perdeu {} dias da sua vida".format(Tempo_perdido))