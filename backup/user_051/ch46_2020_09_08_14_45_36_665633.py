def numero_no_indice(lista):
    i=0
    listan=[]
    while i <= len(lista)-1:
        if lista[i]==i:
            listan.append(i)
        i+=1
    return listan