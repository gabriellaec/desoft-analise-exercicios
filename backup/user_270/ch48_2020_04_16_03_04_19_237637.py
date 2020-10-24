def eh_crescente(l):
    size = len(l)-1
    i = 0
    k = 0
    while i < len(l):
        if k > l[i] :
            return False
            break
        else :
            k = l[i]
        i+=1
    if k == l[size-1] :
        return True