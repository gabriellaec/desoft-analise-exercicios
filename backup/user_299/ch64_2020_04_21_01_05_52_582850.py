def acha_bigramas(string):
    bigramas = []
    for i,e in enumerate(string):
        if i>0:
            bi=string[i-1:i+1]
            print(bi)
            if bi not in bigramas:
                bigramas.append(bi)
    return bigramas