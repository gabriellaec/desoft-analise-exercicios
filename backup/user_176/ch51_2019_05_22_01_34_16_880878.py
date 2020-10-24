def estritamente_crescente(lista):
    crescente = []
    if lista == []:
        crescente = crescente
    else:
        crescente.append(lista[0])
    i = 1
    u = 0
    while i < len(lista):
        while lista[u]<lista[i]:
            u+=1
        if u == i:
            crescente.append(lista[i])
        i+=1
    return crescente