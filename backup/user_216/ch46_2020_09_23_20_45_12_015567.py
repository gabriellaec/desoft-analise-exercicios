
def numero_no_indice(lista):
    nova_lista = []
    for e,i in enumerate(lista):
        if e == i:
            nova_lista.append(i)
    return nova_lista
