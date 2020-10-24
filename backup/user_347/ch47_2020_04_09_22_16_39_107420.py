def estritamente_crescente(lista):
    i = 0
    o = []
    while i < len(lista):
        if lista[i] < lista[i+1]:
            o.insert(0, lista[i])
            i += 1
        else:
            i += 1
    return o
            