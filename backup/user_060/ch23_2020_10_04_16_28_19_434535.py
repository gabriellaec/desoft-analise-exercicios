velocidade = float(input("qual a velocidade?"))
if velocidade > 80:
    multa = (velocidade - 80)*5
    print("multa = {0:.2f}".format(multa))
else:
    print("não foi multado")
                         