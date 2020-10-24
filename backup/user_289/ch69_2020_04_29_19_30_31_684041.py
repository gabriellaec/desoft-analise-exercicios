def junta_listas(lista):
    nova_lista = []
    for e in lista:
        for elemento in e: 
            nova_lista.append(elemento)
    return nova_lista