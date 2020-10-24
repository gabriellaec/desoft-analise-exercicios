velocidade=float(input('qual a velocidadedo seu carro?'))
if velocidade>80:
    multa=5*(velocidade-80)
    print(('voce foi multado em {0:.2f} reais').format(multa))
else:
    print('nao foi multado')