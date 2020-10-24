def estritamente_crescente(lista):
    lista2 = []
    if lista == []:
        return lista2
    else:
        lista2[0] = lista[0]
        i=1
        while i < len(lista):
            if lista[i] > lista2[-1]:
                lista2.append(lista[i])
            i += 1
        return lista2
        