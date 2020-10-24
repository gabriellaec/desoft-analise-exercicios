def pos_arroba(s):
    l = list(s)
    i = 0
    k = 0
    while i<len(l):
        if l[i] == '@':
            k = l
        i+=1
    return k