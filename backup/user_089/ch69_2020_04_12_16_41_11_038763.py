def junta_listas(x):
    y = []
    i = 0
    while i < len(x):
        for e in x[i]:
            y.append(e)
       
        i = i + 1
    return y
    