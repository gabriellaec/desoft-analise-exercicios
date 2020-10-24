def subtracao_de_listas(l1,l2):
    l3 = []
    contador1 = 0
    while contador1 < len(l1):
        if l1[contador1] not in l2:

            l3.append(l1[contador1])
    
        contador1 += 1

    return l3