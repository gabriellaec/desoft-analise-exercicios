def inverte_lista(lista):
    rascunho = []
    tamanho = -1
    for elemento in lista:
        tamanho += 1
    
    while tamanho >= 0:
        rascunho.append(lista[tamanho])
        tamanho -= 1
    lista = rascunho
    return lista