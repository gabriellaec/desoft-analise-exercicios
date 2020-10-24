def movimento(t, S, a):
    t = ((2*s)/a)**(1/2)
    return t

def calcula_tempo(atletas):
    valores = atleta.values()
    chaves = atleta.chaves()
    dic = {}
    for i in chaves:
        t = movimento(t, 100, i)
        for k in atletas:
            if atletas[k] == i:
                dic[k] = t
    return dic