def conta_bigramas(palavra):
    count = list()
    for e in range(0, len(palavra)):
        if len(palavra[e:e+2]) == 2:
            count.append(palavra[e:e+2])
    return count