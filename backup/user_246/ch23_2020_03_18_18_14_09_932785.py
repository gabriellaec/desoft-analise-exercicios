x=int(input('velocidade'))
if x>80:
    print('Mlutado')
    y=(x-80)*5
    print('Valor R${0}'.format(y))
else:
    print('Não foi multado')