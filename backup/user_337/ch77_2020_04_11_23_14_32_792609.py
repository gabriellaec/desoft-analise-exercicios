def movimento(a):
    t = ((200)/a)**(1/2)
    return t

def calcula_tempo(atletas):
    valores = atletas.values()
    chaves = atletas.keys()
    dic = {}
    for i in chaves:
        tempo = movimento(i)
        for k in atletas:
            if atletas[k] == i:
                dic[k] = tempo
    return dic