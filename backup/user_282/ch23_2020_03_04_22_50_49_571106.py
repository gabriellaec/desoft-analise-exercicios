velocidade = int(input('qual eh a velocidade? '))
if velocidade>80:
    print('multa de R${0:.2f}'.format((velocidade-80)*5))
else:
    print('Não foi multado')