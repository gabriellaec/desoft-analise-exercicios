a=int(input("Qual a velocidade do carro?"))
if a>80:
    print ("Voce foi multado, no valor de: R${0:.2f}".format((a-80)*5))
else:
    print("Não foi multado")