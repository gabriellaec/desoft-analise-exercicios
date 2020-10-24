def calcula_tempo(dict):
    saida={}
    for k,v in dict.items():
        saida[k] = ((200*v)**0.5)/v
    return saida