vel = int(input("Qual a velocidade do seu carro? "))

if vel > 80:
    multa = (vel-80)*5
    print("Você foi multado em R$ {0: .2f}.".format(multa))
else:
    print("Não foi multado")