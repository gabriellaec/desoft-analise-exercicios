def estritamente_crescente(lista):
    i = len(lista)-1
    o = []
    while i < len(lista):
        if lista[i] < lista[i+1]:
            o.insert(0, lista[i])
            o.insert(0, lista[i+1])
            i += 1
        else:
            i += 1
    return o
            