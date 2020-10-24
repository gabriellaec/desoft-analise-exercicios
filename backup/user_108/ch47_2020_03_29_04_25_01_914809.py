def estritamente_crescente(lista):
    if len(lista) == 0: return lista
    nova_lista = [lista[0]]
    for item in lista[1:]:
        if item > nova_lista[-1]:
            nova_lista.append(item)
    return nova_lista
          