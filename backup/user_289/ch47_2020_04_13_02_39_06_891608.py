def estritamente_crescente(lista):
    nova_lista = []
    i = 0
    while i <len(lista):
        if not lista[i] in nova_lista:
            nova_lista.append(nova_lista[i])
    return nova_lista
    