velo = float(input("Qual a velocidade do carro? "))

if velo <= 80:
    print("Não foi multado")
else:
    print("Multado. Valor da multa de {0:.2f}".format((velo-80)*5))