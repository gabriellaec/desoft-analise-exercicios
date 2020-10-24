def estritamente_crescente(lista):
    crescente = []
    if lista == []:
        return lista
    else:
        crescente.append(lista[0])
        i = 1
        while i < len(lista):
            if lista[i] >= lista[i-1]:
                crescente.append(lista[i])
                i += 1
            else:
                i += 1
    return crescente