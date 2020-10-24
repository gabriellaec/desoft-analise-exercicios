def estritamente_crescente(lista):
    prox = lista[0]
    seq = [prox]
    cont = 0
    while cont < len(lista):
        if lista[cont] > prox:
            prox = lista[cont]
            seq.append(prox)
            
        cont += 1
    return seq