cigarros = int(input('Quantos cigarros você fuma por dia? '))
anos = int(input('Há quantos anos você fuma? '))
tempo_de_vida_em_min = (cigarros*365*anos)
tempo_de_vida_em_dias = tempo_de_vida_em_min / 1440 
print(tempo_de_vida_em_dias)