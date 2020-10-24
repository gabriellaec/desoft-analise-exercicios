def subtracao_de_listas(lista1,lista2):
    nova_lista = []
    for e in lista1:
        if e not in lista2:
            nova_lista.append(e)
    return nova_lista