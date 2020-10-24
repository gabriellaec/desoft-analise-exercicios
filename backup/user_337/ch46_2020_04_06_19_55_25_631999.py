'''def numero_no_indice(n):
    lista = []
    i = 0
    while i < len(n):
        if n[i]==i:
            lista.append(n[i])
        i+=1
    return lista'''

def numero_no_indice(n):
    lista = []
    indice = 0
    for i in n:
        if i == n[indice]:
            lista.append(i)
        indice+=1
    return lista