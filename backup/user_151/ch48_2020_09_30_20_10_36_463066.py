def eh_crescente(x):
    i = len(x)
    j = 0
    while j < i:
        j += 1
        if x[j] > x[j-1]:
            continue
        else:
            return False
        j += 1
    return True