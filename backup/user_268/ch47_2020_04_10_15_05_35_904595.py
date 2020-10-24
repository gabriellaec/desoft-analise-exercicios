def estritamente_crescente(lista):
    a = len(lista)
    listo = []
    if a == 0:
        return listo
    else:
        listo.append(lista[0])
        for i in range(1, a):
            if lista[i] > lista [i-1]:
                listo.append(lista[i])
            else:
                return listo
        return listo
  