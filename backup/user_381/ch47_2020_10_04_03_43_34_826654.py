def estritamente_crescente(n):
    tamanho = len(n)
    i = 0
    lista_retornada = [0]*tamanho
    while i < tamanho:
        if n[i+1] <= n[i]:
            lista_retornada[i] = n[i+1]
        else:
            lista_retornada[i] = n[i]
    i += 1
    return print(lista_retornada)
