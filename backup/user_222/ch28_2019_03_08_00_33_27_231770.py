velocidade=int(input('Qual é a velocidade?'))
if velocidade>80:
    multa=(velocidade-80)*5
else:
    print('não multado')
print('{:.2f}'.format(multa))
