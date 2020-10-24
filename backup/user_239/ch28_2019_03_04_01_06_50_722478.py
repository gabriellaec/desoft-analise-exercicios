if velocidade>80:
    y=(velocidade-80)*5
    return 'Multa de {0} reais'.format(y)
else:
    return 'Usuário não levou multa'

velocidade=int(input('Qual 
