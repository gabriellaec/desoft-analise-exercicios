x = int(input('Velocidade do carro: ?'))

if x>80:
    print("Voce foi multado: {0}".format((x-80)*5))
else:
    print("Não foi multado")