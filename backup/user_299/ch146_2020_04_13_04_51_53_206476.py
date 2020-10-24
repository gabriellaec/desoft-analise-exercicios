def conta_ocorrencias(s):
    ocorrencias = {}
    for c in s:
        if c in ocorrencias:
            ocorrencias[c] = ocorrencias[c] + 1
        else:
            ocorrencias[c] = 1
    return ocorrencias