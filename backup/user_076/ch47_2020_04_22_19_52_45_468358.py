def estritamente_crescente(lista):
    i = 0
    lista_crescente = []
    if len(lista) > 0:
        lista_crescente.append(lista[i])
    while i+1< len(lista):
        if lista[i+1] > lista[i]:
            lista_crescente.append(lista[i+1])
        i+=1
    return lista_crescente
        