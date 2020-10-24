velocidade=int(input("Qual a velocidade do carro? "))
if velocidade>80:
    print ("Você foi multado em R${0:.2f}".format(5*(velocidade-80)))
else:
    print ("Não foi multado")