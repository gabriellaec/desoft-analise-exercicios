velo = float(input('Qual a velocidade do carro?'))
if velo > 80:
    multa = 5.00*(velo - 80)
    print('você foi multado')
    print('{0:.2f}'.format(multa)
else:
    print('Não foi multado')