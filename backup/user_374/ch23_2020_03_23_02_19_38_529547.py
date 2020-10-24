a = input("Velocidade do carro ")
vel = int(a)

if vel > 80:
    calculo = (vel -80)*5
    print('multado em: R$ {0:.2f}'.format(calculo))

else:
    print('não foi multado')