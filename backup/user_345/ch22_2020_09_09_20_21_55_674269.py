cigarros_por_dia = input ('Quantos cigarros voce fuma por dia: ')
anos_fumando = input ('Ha quantos anos voce fuma: ')
tempo_perdido = (cigarros_por_dia * 365 * anos_fumando) / 144
print ('O seu tempo perdido foram {0} dias'. format (tempo_perdido))