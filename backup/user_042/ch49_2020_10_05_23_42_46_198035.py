lista = []
def inverte_lista(lista):
    i = 0
    n = 1
    lista_nova = []
    while i < len(lista):
        de_tras = lista[i + (len(lista)-n)
        lista_nova.append(de_tras)
        n += 1
        i += 1
    return lista_nova