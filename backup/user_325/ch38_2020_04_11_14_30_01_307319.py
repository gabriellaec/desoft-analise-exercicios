def quantos_uns(n):
    ocorrencias = {}
    i = 0
    while i < len(n):
        if i in ocorrencias:
            ocorrencias[i] = ocorrencias[i] + 1
        else:
            ocorrencias[i] = 1
    return ocorrencias