vel = int(input("Qual a velocidade em km/h do carro? "))
if vel > 80:
    multa = 5*(vel-80)
    print("Multa de {0:.2f}".format(multa))
else:
    print("Não foi multado")