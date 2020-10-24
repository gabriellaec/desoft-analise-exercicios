def filtra_positivos(l1):
    a = len(l1)
    if a == 0:
        return l1
    

    novaLista = []

    for i in l1:
        if i > 0:
            novaLista.append(i)
            

    return novaLista