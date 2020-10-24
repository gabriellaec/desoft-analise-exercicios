velocidade=float(input("qual eh a velocidade:"))
if velocidade>80:
    multa=(velocidade-80)*5
    print("A sua multa foi de {0:.2f}".format(multa))
elif velocidade<=80 :
    print('Não foi multado')