def estritamente_crescente(n):
    tamanho = len(n)
    lista_retornada = []
    if tamanho == 0:
        return []
    lista_retornada.append(n[0])
    primeiro_numero = n[0]
    i = 1
    while i < tamanho:
        if n[i] > primeiro_numero:
            lista_retornada.append(n[i])
        else:
            del n[i]
        i += 1
    return print(lista_retornada)

