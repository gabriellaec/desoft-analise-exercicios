def separa_trios(l):
    s = ''
    for i in range(len(l)):
        if  (i + 1) % 3 == 0:
            s += l[i]+ ','
        else:
            s+= l[i]
    s.split(',')
    return s