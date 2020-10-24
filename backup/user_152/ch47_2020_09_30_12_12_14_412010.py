def estritamente_crescente (lista):
    listanova = []
    i = 0
    size = len(lista)
    size2 = len(listanova)
    if size2 == size:
        listanova = []
    elif i==size:
        listanova.append(lista[i])
    else:
        while i<size:
            seguinte = i+1
            if seguinte <= size:                
                if lista[i]<lista[seguinte]:
                    termo = lista[i]
                    listanova.append(termo)
            i += 1
    return listanova
