velocidade=float(input('velocidade do carro: '))

if velocidade>80:
    print('{0}'.format((velocidade-80)*5))
else:
    print('Não foi multado')