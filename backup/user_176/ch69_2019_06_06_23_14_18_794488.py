def junta_listas(original):
    nova = []
    i=0
    while i<len(original):
        if original[i][i] not in nova:
            nova.append(original[i][i])
            i+=1
    return nova