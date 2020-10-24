veloc = float(input("Qual a velocidade do seu carro(Km/h): "))
if veloc > 80:
    print("Sua multa é de {0:.2f}".format((veloc-80)*5))
else:
    print("Não foi multado")