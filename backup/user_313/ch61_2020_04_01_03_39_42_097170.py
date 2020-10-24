def filtra_positivos(l1):
    a = len(l1)
    if a == 0:
        return l1
    
    indice = 0
    novaLista = [0]*a

    for e in l1:
        if e > 0:
            novaLista[indice] = a
            

        else:
            novaLista.remove(0)

        indice += 1
            

    return novaLista