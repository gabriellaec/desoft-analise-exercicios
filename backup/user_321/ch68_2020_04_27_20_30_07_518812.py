def separa_trios(l):
    s = []
    for i in range(len(l)):
        if  (i + 1) % 3 == 0:
            s.append(l[(i-3):(i+1)])
    return s