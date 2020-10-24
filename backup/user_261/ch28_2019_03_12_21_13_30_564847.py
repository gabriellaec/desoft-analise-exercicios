a= float(input("velocidade do carro:"))
if a>80:
    multa=5*(a-80)
    print("você foi multado e deve pagar {0:.2f}".format(multa))
else:
    print("Não foi multado")
    
    