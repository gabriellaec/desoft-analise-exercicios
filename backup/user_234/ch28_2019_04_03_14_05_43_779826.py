velocidade=(int(input("Qual a velocidade do seu carro?: ")))

if velocidade > 80:
    multa = (velocidade-80)*5
    print("Sua multa foi de {0}".format(multa))
else:
    print("Não foi multado")