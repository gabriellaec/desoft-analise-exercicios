def eh_crescente(l):
    i = 0
    k = 0
    while i < len(l)-1:
        if not k > l[i] :
            return False
            break
        else :
            k = l[i]
        i+=1
    if k == l[len(l)-1] :
        return True