def separa_trios(l):
    l1= []
    i= 0
    while i < len(l):
        l1.append(l[i:i+3])
        i += 3
    return l1