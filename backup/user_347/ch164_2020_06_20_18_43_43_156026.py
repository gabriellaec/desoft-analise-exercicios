def traduz (lista, dic):
    teste = []
    for i in lista:
        if i in dic:
            teste.append(dic[i])
    return teste
    