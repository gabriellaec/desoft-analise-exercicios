def numero_no_indice (listobas):
    listobas = []
    i = 0
    while i < len(listobas):
        if listobas [i] == i:
            listobas.append (i)
        i+=1 
    return listobas