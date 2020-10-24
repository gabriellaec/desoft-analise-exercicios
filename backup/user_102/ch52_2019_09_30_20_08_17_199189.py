def eh_crescente(x):
    if x == []:
        return Ture
    i = 1
    while i<len(x):
        if x[i-1] < x[i] :
            return True
        else:
            return False
