float(velocidade = input('Qual a velocidade do seu carro? '))
if velocidade > 80:
    multa = (5*(velocidade-80))
    print('{0:.2f}'.format(multa)
else:
    multa = 0       
    print('Não foi multado')