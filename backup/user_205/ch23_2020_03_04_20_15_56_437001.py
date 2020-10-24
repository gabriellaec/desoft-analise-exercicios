velocidade = int(input("Qual a velocidade do seu carro: "))
if (velocidade>80):
    print ("Você foi multado!")
    print ("Sua multa é de R$ {0}".format((velocidade-80)*5))
else:
    print ("Não foi multado")