a = float(input("Qual a velocidade do carro? "))
if a > 80:
    print("você foi multado")
    b=5*(a-80)
    print("R$ {0:.2f}".format(b))
else:
    print("você não foi multado")
