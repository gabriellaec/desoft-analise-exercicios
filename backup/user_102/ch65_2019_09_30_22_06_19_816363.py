def acha_bigramas(x):
    i = 0
    d = []
   
    while i < len(x):
        d.append(x[i:(i+1)])
        i += 1
    return d