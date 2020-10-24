def estritamente_crescente(lista):
    crescente = []
    maxim = 0
    for i in lista:
        if lista[i] > maxim:
            lista[i] = maxim
            crescente.append(maxim)
		return crescente