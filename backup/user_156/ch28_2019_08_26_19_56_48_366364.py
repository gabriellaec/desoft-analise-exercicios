x = float(input('Velocidade do carro: ?'))

def calculamulta(x):
    if x>80:
        return "Voce foi multado: {0}".format((x-80)*5)
    else:
        return "Não foi multado"

print("{0:.2f}".format(calculamulta(x)))