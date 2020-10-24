velocidade=float(input('velocidade do carro: '))

if velocidade>80:
    print('você foi multado')
    print('{0}R$'.format((velocidade-80)*5))
else:
    print('Não foi multado')