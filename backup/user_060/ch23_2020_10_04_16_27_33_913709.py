velocidade = float(input("qual a velocidade?"))
if velocidade > 80:
    multa = (velocidade - 80)*5
    return "multa"
    print("multa = {0:.2f}".format(multa))
else:
    return "não foi multado"
                         