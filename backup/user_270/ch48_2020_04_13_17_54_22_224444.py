def eh_crescente(l):
    size = len(l)
    i = 0
    k = 0
    while i < len(l):
        if k > l[i] :
            return False
            break
        else :
            k = l[i]
        i+=1
    if k == l[size] :
        return True