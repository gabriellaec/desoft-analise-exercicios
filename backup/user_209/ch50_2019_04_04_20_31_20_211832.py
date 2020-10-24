def numero_no_indice (listobas):
    listobas = []
    i = 0
    for e in listobas:
        if [e] == [i]:
            listobas.append(e)
            i+=1
    return listobas