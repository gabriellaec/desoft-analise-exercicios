def calcula_media(lista):
    lista = []
    for dic in lista:
        for ele in dic:
            lista.append(dic[ele])
    return sum(lista)/len(lista)