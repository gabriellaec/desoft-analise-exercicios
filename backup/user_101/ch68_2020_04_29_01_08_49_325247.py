def separa_trios(l):
    i = 2
    ll = []
    if len(l) % 3 == 0:
        while i < len(l):
            li = []
            li.append(l[i])
            li.append(l[i-1])
            li.append(l[i-2])
            ll.append(li)
            i += 3
    elif len(l) % 3 == 1:
        
    else:
        
    return ll