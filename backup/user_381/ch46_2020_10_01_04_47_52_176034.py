def numero_no_indice(n):
    i = 0
    tamanho = len(n)
    while i <= tamanho:
        if i == n[i]:
            print(n[i])
        else:
            del n
    return print(n)