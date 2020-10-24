vel = int(input("qual a velocidade do carro? "))
if vel > 80:
    multa = (vel-80)*5
    print("O valor da multa é: R${0:.2f}" .format(multa))
else:
    print('Não foi multado')