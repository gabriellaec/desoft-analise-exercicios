velocidade = int(input("Qual a velocidade deste carro?"))
if velocidade > 80:
    print ("Você foi multado em {0}".format((velocidade*5)-400)
else:
    print ("Não foi multado")