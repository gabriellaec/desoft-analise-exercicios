def primeiras_ocorrencias(a):
    p = []
    ocor = {}
    for ele in range(len(a)):
        if (a[ele:(ele+1)]) not in p:
            p.append(a[ele:(ele+1)])

    for big in p:
        ocor[big] = a.index(big)
    return ocor
