velocidade = int(input('dirigia com qual velocidade? '))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print('Sua multa será: {0:.2f}'.format(multa))

else:
    print('Não foi multado')
