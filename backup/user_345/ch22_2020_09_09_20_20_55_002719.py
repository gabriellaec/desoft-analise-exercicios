cigarros_por_dia = input ('Quantos cigarros voce fuma por dia: ')
anos_fumando = input ('Ha quantos anos voce fuma: ')
tempo_perdido =  cigarros_por_dia * (1/144) * 365 * anos_fumando
print ('O seu tempo perdido foram {0} dias'. format (tempo_perdido))