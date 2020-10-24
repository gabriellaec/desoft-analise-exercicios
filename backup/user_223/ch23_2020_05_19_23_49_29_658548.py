vel = float(input("Insira a velocidade do seu carro: "))
multa = 5*(vel-80)
if vel>80:
    print({:.2f}.format(multa))
else:
    print("Não foi multado")
    