def separa_trios(l):
    s = []
    for i in range(len(l)):
        if  (i + 1) % 3 == 0:
            s.append(l[(i-2):(i+1)])
        elif len(l) - i <= 2:
            s.append(l[i:])
    return s
