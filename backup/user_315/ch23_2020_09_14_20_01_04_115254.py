velocidade = float(input('Insira a velocidade do carro: '))

if velocidade > 80: 
    print ('Você foi multado!')
    multa = (velocidade - 80) * 5
    print ('Você pagará uma multa no valor de R${0:.2f}'.format (multa))

else:
    print('você nao foi multado')