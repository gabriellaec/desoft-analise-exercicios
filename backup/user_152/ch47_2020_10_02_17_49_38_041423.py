def estritamente_crescente (lista):
    listanova = []
    i = 0
    size = len(lista)
    if size > 0:
        listanova.append(lista[i])
        if lista[1]>lista[i]:
            listanova.append(lista[1])
        i = 2    
        while i<size:
            if lista[i] > lista[i-1]:                
                    termo = lista[i]
                    listanova.append(termo)
            i += 1
    return listanova