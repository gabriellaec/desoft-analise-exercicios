def estritamente_crescente (lista):
    listanova = []
    i = 0
    size = len(lista)
    if i==(size-1):
        listanova.append(lista[i])
    else:
        while i<size:
            seguinte = i+1
            if seguinte < size:                
                if lista[i]<lista[seguinte]:
                    termo = lista[i]
                    listanova.append(termo)
            i += 1
    return listanova