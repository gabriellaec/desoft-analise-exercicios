def eh_crescente(x):

    i = 0
    crescente = False
    while i < len(x):
        if x[i] >= x[i-1]:
            crescente = True
        else:
            crescente = False
        i += 1
            

    return crescente