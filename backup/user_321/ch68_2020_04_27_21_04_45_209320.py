def separa_trios(l):
    s = []
    for i in range(len(l)):
        if  (i + 1) % 3 == 0:
            s.append(l[(i-2):(i+1)])
        if len(l) - i <= 2 and len(l)%3!=0:
            s.append(l[i:])
            break
    return s