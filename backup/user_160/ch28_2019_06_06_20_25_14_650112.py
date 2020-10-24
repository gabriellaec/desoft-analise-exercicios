vel = int(input("Qual a velocidade do carro?"))
if vel > 80:
    multa = 5 * (vel - 80)
    print("{0:.2f}".format(multa))
else:
    print("Não foi multado")