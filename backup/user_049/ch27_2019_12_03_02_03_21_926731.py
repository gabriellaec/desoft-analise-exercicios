cigarros_por_dia = int(input('quantos cigarros voce fuma por dia?: '))
anos_fumando = int(input('ha quantos anos fuma?: '))
minutos_perdidos = (cigarros_por_dia*10)*(anos_fumando*365)
dias_perdidos = minutos_perdidos / 1440
#print('você perdeu {0:.0f} dias de vida'.format(dias_perdidos))
print(dias_perdidos)