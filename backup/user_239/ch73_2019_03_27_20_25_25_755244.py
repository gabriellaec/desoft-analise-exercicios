def remove_vogais(x):
    i=0
    while i<len(x):
        if x[i]!='a':
            del x[i]
        i+=1
    return x
