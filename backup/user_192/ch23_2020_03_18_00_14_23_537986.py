v = int(input('Qual a velocidade do carro? '))

if v > 80:
    multa = (v - 80)*5
    print('VocÊ foi multado em R${:.2f} '.format(multa))

else:
    print('Não foi multado')