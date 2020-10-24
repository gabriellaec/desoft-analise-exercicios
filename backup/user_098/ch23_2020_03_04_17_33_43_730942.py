velocidadepega = float(input("Velocidade: "))

if velocidadepega <= 80:
    print("Não foi multado")
else:
    valor = 5*(velocidadepega-80)
    print("Você foi multado em {0:.2f} " .format(valor))