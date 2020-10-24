def conta_bigramas(a):
    p = []
    ocor = {}
    for ele in range(len(a)):
        if len((a[ele:(ele+2)])) == 2:
            if (a[ele:(ele+2)]) not in p:
                p.append(a[ele:(ele+2)])

    for big in p:
        ocor[big] = a.count(big)
    return ocor
