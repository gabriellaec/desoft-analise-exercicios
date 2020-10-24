def calcula_media(lista):
    add = list()
    for i in range(len(lista)):
        for e in range(1, len(lista[i])):
            x = lista[i]["aluno{}".format(e)]
            add.append(x)
    return add