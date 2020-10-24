vel=float(input('velocidade em km'))
if vel>=80:
    valor=(vel-80)*5
    valor=float("{0:.2f}".format(valor))
    print('multa de {} reais'.format(valor))
else:
    print('Não foi multado')
    