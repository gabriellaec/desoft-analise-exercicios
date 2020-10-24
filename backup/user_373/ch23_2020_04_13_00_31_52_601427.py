velocidade= int(input('Velocidade: '))
if velocidade > 80 :
    multa= float(5*(velocidade-80))
    print ('Multa: R$ {0:.2f}'.format(multa))
else:
    print ('sem multa')
    