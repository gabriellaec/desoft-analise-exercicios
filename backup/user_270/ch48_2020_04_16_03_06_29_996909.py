def eh_crescente(l):
    size = len(l)-1
    i = 0
    k = 0
    while i < len(l):
        if l[i] > l[i+1] :
            return False
            break
        else :
            k = l[i]
        i+=1
    if k == l[size] :
        return True