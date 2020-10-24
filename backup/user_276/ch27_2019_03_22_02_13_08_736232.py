n_cigarros = int(input('Quantos cigarros você fuma por dia?   '))
anos_fumando = int(input('Há quantos anos você fuma?   '))
tempo_perdido = (10 * n_cigarros * anos_fumando * 365)/(60*24)
print(tempo_perdido)