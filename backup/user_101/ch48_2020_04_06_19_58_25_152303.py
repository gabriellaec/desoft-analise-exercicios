def eh_crescente(l):
    cresce = True
    i = 1
    while i < len(l):
        if l[i-1] < l[i] and cresce == True:
            cresce =  True
        else:
            cresce = False
        i += 1
    if cresce == True:
        return True
    else:
        return False