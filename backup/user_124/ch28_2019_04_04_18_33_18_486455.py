a = int(input("qual a velocidade do carro: "))
if a > 80:
    y = (80 - a) * 5
    print("o usuario foi multado : R${0:.2f}".format(y))
else:
    print("Não foi multado")
    