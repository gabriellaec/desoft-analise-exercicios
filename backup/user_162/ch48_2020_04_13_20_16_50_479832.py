def eh_crescente(l):
    if len(l) < 2:
        return False
    t_cre = [l[0]]
    for i in range(1,len(l)):
        if l[i] > l[i-1]:
            t_cre.append(l[i])
        else:
            return False
    if t_cre == l:
        return True
    else:
        return False