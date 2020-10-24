dias=int(input('quantos cigarros vc fuma por dia: '))
anos=int(input('por quantos anos? '))
cigarros=dias*365*anos
minutos_perdidos=cigarros*10
dias_perdidos=minutos_perdidos/(24*60)
print('voce perdeu {0} dias'.format(dias_perdidos))