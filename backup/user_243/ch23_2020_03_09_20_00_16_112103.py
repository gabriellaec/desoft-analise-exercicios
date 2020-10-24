velo=float(input ("Qual a velocidade do seu carro?"))
if (velo)>80:
        print ("Você foi multado", "e a multa foi de {0:.2f}".format(((velo-80)*5)))
else:
        print ("Não foi multado")
        