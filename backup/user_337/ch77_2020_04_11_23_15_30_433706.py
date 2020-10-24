def calcula_tempo(atletas):
    valores = atletas.values()
    chaves = atletas.keys()
    dic = {}
    for i in chaves:
        tempo = (200/i)**(1/2)
        for k in atletas:
            if atletas[k] == i:
                dic[k] = tempo
    return dic