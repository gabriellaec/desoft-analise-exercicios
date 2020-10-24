def estritamente_crescente(lista):
    maxi = lista[0]
    l = [maxi]
    i = 0
    while i<len(lista)-1:
        if lista[i+1] > maxi:
            maxi = lista[i+1]
            l.append(lista[i+1])
        i+=1
    return l