a = input('quantos cigarros por dia?')
b = input('há quantos anos fuma?')

cigarros_na_vida = a * (b * 365)
total_minutos = cigarros_na_vida * 10 
dias_perdidos = total_minutos / 60 / 24

print(dias_perdidos)