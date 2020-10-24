def calcula_tempo(entrada):
    saida={}
    for k, v in entrada.items():
        saida[k] = ((200/v)**(1/2))
    return saida
        