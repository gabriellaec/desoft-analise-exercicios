velocidade = int(input("Qual a velocidade do carro?:"))

if velocidade > 80:
    multa = (velocidade - 80) * 5
    print("Você foi multado em:" "{0:.2f}".format(multa))