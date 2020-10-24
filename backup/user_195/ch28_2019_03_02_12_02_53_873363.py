velocidade=int(input("qual sua velocidade?"))
if velocidade <=80:
    print("boa viagem")
else:
    multa=(velocidade-80)*5
    print("sua multa é de {0}".format(multa))