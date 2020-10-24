def estritamente_crescente(lista):
    a = len(lista)
    listo = []
    if a == 0:
        return listo
    else:
        listo.append(lista[0])
        for i in range(0, a):
            if lista[i+1] > listo[i]:
                listo.append(lista[i+1])
        return listo
  