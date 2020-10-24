velocidade=int(input("Qual a velocidade do carro?"))
multa=5*(velocidade-80)
if velocidade>80:
    print ("Se fodeu, foi multado em R${0:.2f}".format(multa))
else:
    print("Não foi multado")