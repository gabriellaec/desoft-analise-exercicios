def estritamente_crescente (lista):
    listanova = []
    i = 0
    size = len(lista)
    ##primeiro = lista[i]
    ##listanova.append(primeiro)
    while size>i:
        termo = lista[i]
        listanova.append(termo)
        while i<size:
            i = 1
            if lista[i]<lista[i+1]:
                termo = lista[i]
                listanova.append(termo)
    return listanova