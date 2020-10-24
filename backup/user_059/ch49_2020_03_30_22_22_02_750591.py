def inverte_lista(lista):
    lx = [0]*len(lista)
    i = len(lista)
    j = 0
    while 0<i<=len(lista):
        lx[j] = lista[i-1]
        i-=1
        j+=1
    return lx
