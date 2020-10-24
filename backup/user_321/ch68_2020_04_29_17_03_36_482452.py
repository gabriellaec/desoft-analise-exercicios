def separa_trios(l):
    s = []
    for i in range(len(l)):
        if  (i + 1) % 3 == 0:
            s.append(l[(i-2):(i+1)])
    if l[-1] in s:
        return s
    elif l[-2] in s:
        s.append(l[-2:-1])
    else:
        s.append(l[-1])
    return s