def estritamente_crescente(n):
    tamanho = len(n)
    i = 0
    lista_retornada = []
    while i < tamanho:
        if n[i+1] < n[i]:
            lista_retornada.append(n[i+1])
    i += 1
    return print(lista_retornada)

