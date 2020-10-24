def quantos_uns(x):
    w= str(x)
    i= 0
    conta= 0
    while i<len(x): 
        if w[i] in '1':
            conta+=1
            i+= 1
    return conta         