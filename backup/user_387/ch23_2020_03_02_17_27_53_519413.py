velocidade = float(input('d :'))

if velocidade > 80:
    multa = (velocidade - 80) * 5

    print('Foi multado')
    print("{0:.2f}".format(multa))

else:
    print('Não foi multado')

 