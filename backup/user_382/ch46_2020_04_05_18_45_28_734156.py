lista = []
def numero_no_indice(l1):
    for i in range(l1):
        if i == l1[i]:
            lista.append(i) 
    return lista

