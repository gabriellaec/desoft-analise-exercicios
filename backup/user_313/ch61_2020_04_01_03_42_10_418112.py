def filtra_positivos(l1):
    a = len(l1)
    if a == 0:
        return l1
    
    indice = 1
    novaLista = [0]*a

    for i in l1:
        if i > 0:
            novaLista[indice-1] = i
            

        else:
            novaLista.remove(0)

        indice += 1
            

    return novaLista