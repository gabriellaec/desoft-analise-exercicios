def estritamente_crescente(lista):
    seq = []
    if len(lista) > 0:
        prox = lista[0]
    else:
        return seq
    seq = [prox]
    cont = 0
    while cont < len(lista):
        if lista[cont] > prox:
            prox = lista[cont]
            seq.append(prox)
            
        cont += 1
    return seq