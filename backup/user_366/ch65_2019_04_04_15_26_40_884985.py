def acha_bigramas(string):
    bigramas = []
    i = 0 
    while i < len(string):
        if string[i:(i+2)] in bigramas:
            i += 1
        else:
            bigramas.append(string[i:(i+2)])
            i += 1
    del bigramas[len(bigramas)-1] 
    return bigramas