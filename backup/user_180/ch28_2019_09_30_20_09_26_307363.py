velocidade_carro = int(input("Quala velocidade do carro? (km/h): "))
if velocidade_carro > 80:
    print("Você foi multado em {0:.2f} reais.".format(velocidade_carro - 80))