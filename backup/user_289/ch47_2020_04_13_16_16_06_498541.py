def estritamente_crescente(lista):
    nova_lista = []
    nova_lista[0] = lista[0]
    maior = lista[0]
    for e in lista:
        if e > maior:
            if e not in nova_lista:
                nova_lista.append(e)
            maior = e
    return nova_lista
    