def estritamente_crescente(lista):
    a = len(lista)
    listo = []
    if a == 0:
        return listo
    else:
        listo.append(lista[0])
        for i in range(1, a):
            for j in range (i):
                if lista[i] > listo[j] and lista[i] < lista[j + 2]:
                    listo.append(lista[i])
        return listo
    