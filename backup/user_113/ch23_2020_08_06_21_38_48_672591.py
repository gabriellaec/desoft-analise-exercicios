veloc = int(input("Qual a velocidade do carro?: "))
if veloc > 80:
    print("Vc foi multado, chola mais")
    multa = ((veloc - 80)*5)
    print("Sua multa foi de {0}".format(round(multa,2)))
else:
    print("Não foi multado")