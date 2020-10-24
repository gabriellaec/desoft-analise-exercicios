velocidade = float(input('Qual a sua velocidade? '))

if velocidade > 80:
    multa = format((velocidade - 80)*5,'.2f')
    print('Voce foi multado em R$ {0}'.format(multa))
