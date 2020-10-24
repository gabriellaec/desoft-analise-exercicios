x = int(input("qual a velocidade do carro ? "))
if x <= 80:
    print("Não foi multado")
if x > 80:
    print("Você foi multado por: {0:.2f}".format(5 * (x - 80)))