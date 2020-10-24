velocidade=float(input("qual sua velocidade?"))
if velocidade>80:
    multa=(velocidade-80)*5
    print("voce foi multado no valor de {:.2f}".format(multa))