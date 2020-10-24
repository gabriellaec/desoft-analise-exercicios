def calcula_tempo(dic_atletas):
    dic = dic_atletas
    saida = {}
    for k,v in dic.items():
        saida[k] = (200/v)**(1/2)
    return saida