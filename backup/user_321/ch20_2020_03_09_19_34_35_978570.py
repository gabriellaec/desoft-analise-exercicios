km = int (input('Distancia em km: '))

if (km<= 200):
    print('O preço da viagem é R$:{0:.2f}'.format(km*0.5))
else:
    print('O preço da viagem é R$:{0:.2f}'.format(km*0.45))