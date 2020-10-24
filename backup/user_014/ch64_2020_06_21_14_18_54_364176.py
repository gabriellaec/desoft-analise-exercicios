def acha_bigramas(string):
    i = 0
    conta_bigramas = []
    while i < len(string) - 1:
        if string[i] + string[i+1] not in conta_bigramas:
            conta_bigramas.append(string[i] + string[i+1])
        i += 1
    return conta_bigramas