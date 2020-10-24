def monta_mala(L1):
    c = 0
    i = 0
    m = []
    if sum(L1) <=23:
        return L1
    else:
        while(i <= len(L1)):
            m.append(L1[c])
            if sum(m) > 23:
                del m[c]
                return m
            i += 1
            c += 1