def estritamente_crescente(lista):
    if len(lista) == 0:
        return lista
    else:
        l_crescente = [lista[0]]
        i = 1
        n = lista[0]
        while i < len(lista):
            if lista[i] > n:
                n = lista[i]
                l_crescente.append(n)
            i += 1
    return l_crescente

def eh_crescente(l_crescente):
    if len(lista) == len(l_crescente):
        return True
    else:
        return False