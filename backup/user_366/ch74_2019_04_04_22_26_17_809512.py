def conta_bigramas(string):
    dicio = {}
    i = 0
    while i < (len(string)-1):
        a = string[i:(i+2)]
        if a in dicio:
            dicio[a] += 1
        else:
            dicio[a] = 1
        i += 1
    return dicio