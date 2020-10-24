def eh_crescente(l):
    if len(l) == 0:
        return False
    ec = []
    i = 0
    else:
        ec.append(l[0])
        while i < len(l):
            if l[i] > ec[-1]:
                ec.append(l[i])
        if ec = l:
            return True
        else:
            return False