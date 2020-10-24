def eh_crescente(l):
    if l == []:
        return False
    else:
        lc = [l[0]]
        for i in range(1,len(l)):
            if l[i] > lc[-1]:
                lc.append(l[i])
            else:
                return False
                break
        if lc == l:
            return True