def estritamente_crescente (lista):
    listanova = []
    i = 0
    size = len(lista)
    if size > 0:
        listanova.append(lista[0])
        if lista[i+1]>lista[i]:
            listanova.append(lista[i+1])
            ult = listanova[1]
            i = 2    
            while i<size:
                if lista[i] > ult:
                        ult = lista[i]
                        termo = lista[i]
                        listanova.append(termo)
                i += 1
    return listanova