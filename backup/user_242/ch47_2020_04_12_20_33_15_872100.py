def estritamente_crescente(lista1):
    if lista1 ==[]:
        return lista1
    else:
        maximo = lista1[0]
        lista = [maximo]
        i = 0
        for i in range(len(lista1)-1):
            if lista1[i+1] > maximo:
                maximo = lista1[i+1]
                lista.append(lista[i+1])
        return lista