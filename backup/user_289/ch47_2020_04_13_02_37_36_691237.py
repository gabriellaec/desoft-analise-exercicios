def estritamente_crescente(lista):
    nova_lista = lista.sort()
    nova_lista2 = []
    i = 0
    while i <len(nova_lista):
        if not nova_lista[i] in nova_lista2:
            nova_lista2.append(nova_lista[i])
    return nova_lista2
    