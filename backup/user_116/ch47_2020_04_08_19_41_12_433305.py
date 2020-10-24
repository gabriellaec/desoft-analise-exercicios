def estritamente_crescente(lista):
    listan=[]
    u=1
    i=0
    listan.append(lista[0])
    while u < len(lista):
        if lista[u]>=lista[i]:
            if lista[u] not in listan:
                listan.append(lista[u])
                u+=1
                i+=1
            else:
                u+=1
                i+=1
        else:
            u+=1
            i+=1
    return listan