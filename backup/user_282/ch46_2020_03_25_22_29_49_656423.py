lista1 = []

def numero_no_indice(lista):
    i = 0
    while i<len(lista):
        if lista[i]==i:
            lista1.append(lista[i])
        i += 1
    else:
        return(lista1)