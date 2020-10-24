def estritamente_crescente(lista):
    i=0
    maximo=lista[0]
    resp=[maximo]
    while i < len(lista):
        if lista[i+1] > maximo:
            maximo = lista[i=1]
            resp.append(lista[i+1])
        i+=1
    return resp