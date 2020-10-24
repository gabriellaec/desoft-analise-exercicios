def calculamulta(x):
    x = input('Velocidade do carro: ?')
    if x>80:
        return "Voce foi multado: {0}".format((x-80)*5)
    else:
        return "Não foi multado"
    print("{0:.2f}".format(calculamulta(x)))