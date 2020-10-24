def numero_no_indice (listobas):
    listobas = []
    i = 0
    for e in listobas:
        if listobas[i] == i:
            listobas.append(e)
        i+=1
    return listobas