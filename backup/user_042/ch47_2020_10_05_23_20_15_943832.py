lista = []
def estritamente_crescente(lista):
    lista_sequencia[0] = lista[0]
    i = 1
    while i < len(lista):
        if lista[i] > lista[i-1]:
            lista_sequencia.append(lista[i])
        i += 1
    return lista_sequencia