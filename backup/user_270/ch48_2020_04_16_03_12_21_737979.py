def eh_crescente(l):
    t=0
    for i in range(len(l)-1):
        if l[i]>l[i+1] :
            return False
            break
        else:
            t += 1
    if t == len(l):
        return True