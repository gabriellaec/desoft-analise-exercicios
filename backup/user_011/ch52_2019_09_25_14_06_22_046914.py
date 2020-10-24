def eh_crescente(lista):
    if len(lista) == 0:
        return True
    else:
        l_crescente = [lista[0]]
        i = 1
        n = lista[0]
        while i < len(lista):
            if lista[i] > n:
                n = lista[i]
                l_crescente.append(n)
            i += 1
    if len(l_crescente) == len(lista):
        return True
    else:
        return False
