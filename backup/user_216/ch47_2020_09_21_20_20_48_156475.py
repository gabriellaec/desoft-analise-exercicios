def estritamente_crescente(lista):
    nova_lista = []
    i = 0
    while i < len(lista):
        if i == 0:
            nova_lista.append(lista[i])
            i += 1
        else:
            if lista[i] > lista[i-1]:
                nova_lista.append(lista[i])
            i += 1
    return nova_lista