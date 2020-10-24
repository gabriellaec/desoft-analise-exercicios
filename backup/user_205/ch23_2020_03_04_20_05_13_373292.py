velocidade = int(input("Qual a velocidade do seu carro: "))
if (velocidade>80):
    print ("Sua multa é de {0}".format((velocidade-80)*5))
else:
    print ("Não foi multado")