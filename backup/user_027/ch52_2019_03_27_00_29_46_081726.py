def eh_crescente(x):
    if len(x) == 1:
        return True
    for i in range(1,len(x)):
        if x[i] < x[i-1]:
            return False
    return True