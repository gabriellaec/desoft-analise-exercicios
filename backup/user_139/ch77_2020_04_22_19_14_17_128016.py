def calcula_tempo (atletas):
    dic = {}
    for nome, aceleração in atletas.items():
        tempo = v / aceleração
        dic[nome] = tempo
    return atletas