def conta_bigramas(string):
    dict = {}
    i = 0
    while i < len(string):
        bigrama = string[i:i+2]
        if bigrama not in dict:
            dict[bigrama] = 1
            i += 1
        else:
            dict[bigrama] += 1
            i += 1
    return dict