x = int(input('qual a velocidade?'))
if x > 80:
    multa = (x-80)*5
    print('voce foi multado em {0:.2f}'.format(multa))
if x <= 80:
    print('Não foi multado')

    