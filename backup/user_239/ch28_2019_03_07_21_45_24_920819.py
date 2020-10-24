velocidade=int(input('Velocidade do carro?'))
if velocidade>80:
    y=(velocidade-80)*5
    print('Multa de {0} reais'.format(y))
else:
    print('Usuário não levou multa')

