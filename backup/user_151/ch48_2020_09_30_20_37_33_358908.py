def eh_crescente(x):
    i = len(x)
    j = 1
    while j < i:
        
        if x[j] > x[j-1]:
            j = j + 1
            continue
        else:
            return False
        
    return True