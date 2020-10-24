def separa_trios(lista):
    trios = []
    rascunho = []
    cont = 0
    
    while cont < len(lista):
        if cont % 3 == 0 and cont > 0:
            trios.append(rascunho.copy())
            rascunho.clear()
        rascunho.append(lista[cont])
        cont += 1
        if cont == (len(lista)):
            trios.append(rascunho.copy())
    return trios