velocidade=float(input("qual sua velocidade?"))
if velocidade>80:
    multa = (velocidade-80)*5
    print('{0:.2f}'.format(multa))
else:
    print('Não foi multado')