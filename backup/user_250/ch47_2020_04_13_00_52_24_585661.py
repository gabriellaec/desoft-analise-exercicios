def estritamente_crescente(lista):
    listaC = []
    if lista == []:
        return listaC
    else:
        listaC.append(lista[0])
        i = 1
        while i < len(lista)-1:
            if lista[i] > lista[i-1]:
                listaC.append(lista[i])
            i += 1
        return listaC