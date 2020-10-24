speed = float(input("Velocidade do carro em kilometros?"))

if speed > 80:
    charge = (speed - 80) * 5.00
    print("{0:.2f}".format(charge))
else:
    print("Não foi multado")
