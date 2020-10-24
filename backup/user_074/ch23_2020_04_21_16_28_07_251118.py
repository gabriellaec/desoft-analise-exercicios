vel=int(input('vel em km'))
if vel>80:
    valor=(vel-80)*5
    print('multado')
    print('valor da multa {} reais'.format(valor))
else:
    print('Não foi multado')
    