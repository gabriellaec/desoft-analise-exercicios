velocidade=int(input('Qual é a velocidade?'))
if velocidade>80:
    multa=(velocidade-80)*5
print('{:.2f}'.format(multa))
