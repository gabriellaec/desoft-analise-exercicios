velocidade=float(input("qual sua velocidade?"))
if velocidade>80:
    multa=(velocidade-80)*5
    print("Você foi multado")
    print("{:.2f}".format(multa))