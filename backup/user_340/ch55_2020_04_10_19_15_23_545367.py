def encontra_maximo(matriz):
    i=0
    M=0
    while i<len(matriz):
        for t in matriz[i]:
            if t>M:
                M=t
    return M
        