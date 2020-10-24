def calcula_media(lista):
    l = []
    for dic in lista:
        for ele in dic:
            l.append(dic[ele])
    if len(l) != 0:
        return sum(l)/len(l)
    return 0