def estritamente_crescente(n):
    tamanho = len(n)
    lista_retornada = []
    if tamanho == 0:
        return []
    lista_retornada.append(n[0])
    maior = n[0]
    i = 1
    while i < tamanho:
        if n[i] > maior:
        lista_retornada.append(n[i])
        maior = n[i]
        i += 1
    return print(lista_retornada)

