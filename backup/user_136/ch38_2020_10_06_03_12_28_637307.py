def quantos_uns(x):
    i= 0
    conta= 0
    while i<len(x): 
        if x[i] in '1':
            conta+=1
        i+= 1
    return conta         