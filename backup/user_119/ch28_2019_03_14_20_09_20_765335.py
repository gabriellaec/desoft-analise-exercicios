vel=int(input('Qual a velocidade? '))
if vel>80:
    y=(vel-80)*5
    print('multa de {0.:2f}'.format(y)
else:
    print('Não foi multado')