def estritamente_crescente(lista):
    listaC = []
    if lista == []:
        return listaC
    else:
        listaC.append(lista[0])
        lista[0] = max
        i = 1
        while i < len(lista)-1:
            if lista[i] > max:
                max = lista[i]
                listaC.append(lista[i])
            i += 1
        return listaC