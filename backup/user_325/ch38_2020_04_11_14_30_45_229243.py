def quantos_uns(n):
    ocorrencias = {}
    i = 0
    while i < n:
        if i in ocorrencias:
            ocorrencias[i] = ocorrencias[i] + 1
        i += 1
    return ocorrencias