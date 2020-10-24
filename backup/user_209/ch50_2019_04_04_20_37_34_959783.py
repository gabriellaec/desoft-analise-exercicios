def numero_no_indice (listobas):
    conta = []
    i = 0
    while i < len(listobas):
        if listobas [i] == i:
            conta.append (i)
        i+=1 
    return conta