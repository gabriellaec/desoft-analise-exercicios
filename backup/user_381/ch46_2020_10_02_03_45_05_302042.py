def numero_no_indice(n):
    i = 0
    lista_nova = []
    tamanho = len(n)
    while i < tamanho:
        if i == n[i]:
            lista_nova.append(i)
        i += 1
    return lista_nova