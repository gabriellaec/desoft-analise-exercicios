def estritamente_crescente(lista):
    noval = []
    i = 0
    while i<len(lista):
        x = 1
        if lista[x]>lista[i]:
            noval.append(lista[i])
        else:
            pass
        i+=1
        x+=1
    return noval
