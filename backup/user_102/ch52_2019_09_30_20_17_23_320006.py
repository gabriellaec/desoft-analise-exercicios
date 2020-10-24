def eh_crescente(x):
    i = 1
    while i<len(x):
        if x[i-1] < x[i] :
            i +=1
            continue
        else:
            return False
    return True
