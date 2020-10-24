v = int(input("Qual foi a velocidade do carro? "))

if v > 80:
    print("R${0:.2f}".format((v - 80) * 5))
else:
    print("Não foi multado")