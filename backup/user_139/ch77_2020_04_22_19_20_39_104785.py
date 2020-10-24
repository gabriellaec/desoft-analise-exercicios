def calcula_tempo (atletas):
    dic = {}
    for nome, aceleração in atletas.items():
        tempo = (200 / aceleração) ** (1/2)
        dic[nome] = tempo
    return dic