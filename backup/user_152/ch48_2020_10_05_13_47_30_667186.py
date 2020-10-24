def estritamente_crescente (lista):
    listanova = []
    i = 0
    size = len(lista)
    if size > 0:
        listanova.append(lista[0])
        ult = listanova[0]
        i = 1
        while i<size:
            if lista[i]>ult:
                listanova.append(lista[i])
                ult = lista[i]
                i = 2    
                while i<size:
                    if lista[i] > ult:
                            ult = lista[i]
                            termo = lista[i]
                            listanova.append(termo)
                    i += 1
            i += 1            
    return listanova

def eh_crescente (l):
    if len(estritamente_crescente(l)) == len(l):
        return True
    else:
        return False