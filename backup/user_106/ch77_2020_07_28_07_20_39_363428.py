def calcula_tempo(dic):
    novo = {}
    for i in dic:
        novo[i] = (200 / dic[i]) ** 0.5
    return novo