def eh_crescente(x):
    i = 1
    while i<len(x):
        if x[i-1] < x[i] :
            continue
        else:
            return False
    return True
