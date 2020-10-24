def quantos_uns (x):
    x = str (x)
    i = 0
    ocorrencias = 0
    while i < len(x):
        if x[i] == '1':
            ocorrencias += 1
            i += 1
        else:
            i += 1
    return ocorrencias