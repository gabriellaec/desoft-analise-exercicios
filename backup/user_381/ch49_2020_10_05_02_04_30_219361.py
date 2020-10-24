def inverte_lista(n):
    tamanho = len(n)
    lista_reversa = []
    i = 0
    while i < (tamanho - 1):
        lista_reversa.append(n[tamanho - 1])
        lista_reversa.append(n[tamanho - 1 - i])
        i += 1
    return lista_reversa
    