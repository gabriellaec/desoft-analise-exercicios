def radar_de_velocidade (velocidade):
    if (velocidade < 80):
        return("velocidade razoavel")
    else:
        multa = (velocidade - 80) * 5
        return("O senhor foi multado! O preco eh {0:.2f} reais".format(multa))
velocidade = int(input("Sua velocidade "))

print(radar_de_velocidade(velocidade))