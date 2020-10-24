x=int(input('velocidade'))
if x>80:
    print('Mlutado')
    y=(x-80)*5
    print('{0:.2f}'.format(y))
else:
    print('Não foi multado')