def eh_crescente(l):
    ec = []
    i = 0
    if len(l) == 0:
        return False
    else:
        ec.append(l[0])
        while i < len(l):
            if l[i] > ec[-1]:
                ec.append(l[i])
            i+=1
        if ec == l:
            return True
        else:
            return False