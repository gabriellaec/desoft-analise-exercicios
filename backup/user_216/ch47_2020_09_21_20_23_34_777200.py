def estritamente_crescente(lista):
    nova_lista = []
    i = 0
    c = 0
    while i < len(lista):
        if i == 0:
            nova_lista.append(lista[i])
            i += 1
            c += 1
        else:
            if lista[i] > nova_lista[c-1]:
                nova_lista.append(lista[i])
                c += 1
            i += 1
    return nova_lista
