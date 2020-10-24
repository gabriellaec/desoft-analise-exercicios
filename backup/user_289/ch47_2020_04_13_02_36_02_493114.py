def estritamente_crescente(lista):
    nova_lista = lista.sort()
    nova_lista2 = []
    for i in nova_lista:
        if not i in nova_lista2:
            nova_lista2.append(nova_lista[i])
    return nova_lista2
    