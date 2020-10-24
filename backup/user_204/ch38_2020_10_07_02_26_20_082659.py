def quantos_uns(str(numero)):
    i = 0
    ocorrencias = 0
    while i < len(str(numero)):
        if numero[i] == 1:
            ocorrencias += 1
        i += 1
    return ocorrencias