um = int(input("Qual a velocidade do carro(em km/h)?"))
if um > 80:
    a = (um-80)*5
    print("Você foi multado. A multa é de{0:.2f}".format(a))
else:
    print("Não foi multado")