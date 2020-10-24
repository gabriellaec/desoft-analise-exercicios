def estritamente_crescente(lista):
    i = 0
    o = []
    while i < len(lista):
        if lista[i] < lista[i+1]:
            o.insert((i), lista[i])
            o.insert((i+1), lista[i+1])
            i += 1
        else:
            i += 1
    return o
            