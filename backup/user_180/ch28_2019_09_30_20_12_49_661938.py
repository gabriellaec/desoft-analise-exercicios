velocidade_carro = int(input("Quala velocidade do carro? (km/h): "))
if velocidade_carro > 80:
    print("Você foi multado em {0:.2f} reais.".format(5*(velocidade_carro - 80)))
else:
    print("Não foi multado")