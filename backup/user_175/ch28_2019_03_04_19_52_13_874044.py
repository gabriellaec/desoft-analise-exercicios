velocidade = float(input())

if velocidade > 80:
    multa = (velocidade - 80)*5
    print('Você foi multado, no valor de: R${:.2f}' .format(multa))
else:
    print('Velocidade regular')