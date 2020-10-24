def estritamente_crescente (lista):
    listanova = []
    i = 0
    size = len(lista)
    if i==size:
        termo = lista[i]
        listanova.append(termo)
    while i<size:
        i = 0
        seguinte = i+1
        if lista[i]<lista[seguinte]:
            termo = lista[i]
            listanova.append(termo)
        i += 1
    return listanova