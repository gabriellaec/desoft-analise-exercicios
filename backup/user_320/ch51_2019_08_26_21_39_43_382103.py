def estritamente_crescente(lista):
    prox = lista[0]
    seq = [prox]
    for numero in lista:
        if numero > prox:
            prox = numero
            seq.append(prox)
            
    return seq