#1 cigarro = -10 minutos
#1 ano = 365 dias = x cigarros*10*365
cigarros=int(input('Quantos cigarros você fuma por dia? '))
anos=int(input('Há quantos anos você fuma? '))
diasperdidos=(cigarros*10*anos*365)/(24*60)
print('Parabéns, você perdeu {0} dias de vida!'.format(diasperdidos))