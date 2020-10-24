def lista_sufixos(lista):
    sufix = list()
    for i in range(len(lista)):
        sufix.append(lista[i:len(lista)])
    return sufix