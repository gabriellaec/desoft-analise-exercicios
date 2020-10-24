def numero_no_indice(l_n):
    i = 0
    l_indices = []
    while i < len(l_n):
        if i == l_n[i]:
            l_indices.append(i)
        i+=1
    return l_indices
