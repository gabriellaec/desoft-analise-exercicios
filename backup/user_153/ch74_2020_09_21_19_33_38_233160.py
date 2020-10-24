def conta_bigramas(string):
    bigramas = {}
    idx = 0
    while idx < len(string)-1:
        if string[idx:idx+2] in bigramas:
            bigramas[string[idx:idx+2]] += 1
        else:
            bigramas[string[idx:idx+2]] = 1
        idx += 1
    return bigramas

# bigramas = conta_bigramas("banana nanica")
# print(bigramas)