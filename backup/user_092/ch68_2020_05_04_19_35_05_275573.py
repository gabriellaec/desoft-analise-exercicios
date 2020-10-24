def separa_trios(x):
    if len(x)%3 == 0:
        i = 0
        L1 = []
        L2 = []
        while i < len(x):
            L1.append(x[i])
            L1.append(x[i + 1])
            L1.append(x[i + 2])
            L2.append(L1)
            L1 = []
            i += 3
        return L2
    elif len(x)%3 == 2:
        c = 0
        L3 = []
        L4 = []
        while(c < (len(x)-2)):
            L3.append(x[i])
            L3.append(x[i + 1])
            L3.append(x[i + 2])
            L4.append(L3)
            L3 = []
            c += 3
        L3.append(x[len(X)-1])
        L3.append(x[len(x)])
        L4.append(L3)
        return L4
    else:
        j = 0
        L5 = []
        L6 = []
        while(j < (len(x)-1)):
            L5.append(x[i])
            L5.append(x[i + 1])
            L5.append(x[i + 2])
            L6.append(L5)
            L5 = []
            j += 3
        L5.append(x[len(x)])
        L6.append(L5)
        return L6