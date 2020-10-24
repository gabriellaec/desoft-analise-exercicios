def conta_bigramas(string):
    dc = dict()
    for i in range(len(string)-1):
        dc[string[i:i+2]] = 0
    for i in range(len(string)-1):
        dc[string[i:i+2]] += 1
    return dc
    