def inverte_lista(n):
    tamanho = len(n)
    lista2 = []
    i = 1
    while i <=tamanho:
        lista2.append(n[tamanho-i])
        i = i + 1
    return lista2