def encontra_maximo(lista):
    x = 0
    for n in len(lista):
        for m in len(lista[n]):
            if m>x:
                x = m
    return m