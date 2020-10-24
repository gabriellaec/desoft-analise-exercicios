velocidade= int(input("qual sua velocidade?"))
if velocidade > 80:
    print("você foi multado")
    multa= (velocidade-80)*5
    print("e deverá pagar uma multa de {:.2f} reais".format(multa))
else: 
    print("não foi multado")
    