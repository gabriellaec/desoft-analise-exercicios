def eh_crescente(x):
    i = len(x)
    j = 1
    while j < i:
        if x[j] > x[j-1]:
            return True
        else:
            return False