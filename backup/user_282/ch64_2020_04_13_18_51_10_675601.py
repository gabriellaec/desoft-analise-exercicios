def acha_bigramas(palavra):
    count = list()
    for e in range(len(palavra)):
        if palavra[e:e+2] not in count and len(palavra[e:e+2]) == 2:
            count.append(palavra[e:e+2])
    return count