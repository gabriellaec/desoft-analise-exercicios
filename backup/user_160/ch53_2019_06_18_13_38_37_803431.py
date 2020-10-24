def inverte_lista(n):
    tamanho = len (n)
    lista = []
    i = 1
    while i >= tamanho:
        lista.append(n[tamanho-i])
        i+=1
    return lista
        
    