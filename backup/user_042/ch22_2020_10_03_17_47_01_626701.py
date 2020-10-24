quantos_cigarros = int(input('Quando cigarros fuma por dia?'))
anos_fuma = int(input('A quandos anos fuma?'))

total_cigarros = (quantos_cigarros*365)*anos_fuma
tempo_pertido = ((total_cigarros*10)/60)/24
print('O tempo de vida perdido foi de {0} horas'.format(tempo_pertido))