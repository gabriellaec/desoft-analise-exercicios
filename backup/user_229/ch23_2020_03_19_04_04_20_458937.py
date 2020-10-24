velocidade = input("Qual a velocidade do seu carro? ")
if velocidade > 80:
    print ("Vc foi multado em {:.2f}".format(5*(velocidade-80)))
else:
    print("Não foi multado")
