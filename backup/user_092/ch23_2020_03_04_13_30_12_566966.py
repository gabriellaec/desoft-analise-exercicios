a = int(input('qual a velocidade:'))
if a>80:
    b = (a-80)*5
    print('foi multado, valor R$ {0:.2f}'.format(b))
else:
    print('Não foi multado')