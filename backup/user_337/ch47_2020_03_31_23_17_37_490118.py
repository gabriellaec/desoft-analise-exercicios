def estritamente_crescente(lista):
    i = 1
    while i<=len(lista):
        if lista[i+1] <= lista[i]:
            del lista[i+1]
            print(lista)
        i += 1
        return lista
