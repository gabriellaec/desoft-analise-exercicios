def estritamente_crescente(lista):
    if lista == []:
        return lista
    else:
        inicial = lista[0]
        lista_crescente = [inicial]
        for i in range(len(lista)-1):
            if lista[i+1] > inicial:
                inicial = lista[i+1]
                lista_crescente.append(lista[i+1])
        return lista_crescente