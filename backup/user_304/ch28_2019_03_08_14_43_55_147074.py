a=float(input('qual é a velocidade do seu carro? '))
if a>80:
    v=(a-80)*5
    print('sua multa foi de {0:.2f}'.format(v))
else:
    print ('Não foi multado')
