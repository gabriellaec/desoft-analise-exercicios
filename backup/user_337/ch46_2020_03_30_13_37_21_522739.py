def numero_no_indice(n):
    lista = []
    while i < len(n):
        if n[i]==i:
            lista.append(n[i])
        i+=1
    return lista