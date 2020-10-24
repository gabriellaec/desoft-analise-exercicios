veloc = int(input("Qual a velocidade do carro?: "))
if veloc > 80:
    multa = ((veloc - 80)*5)
    print("Sua multa foi de {0}".format(multa))
else:
    print("Não foi multado")