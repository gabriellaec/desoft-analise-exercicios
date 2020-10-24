def separa_trios(l):
    i = 0
    ll = []
    while i < len(l):
        ll.append(l[i:(i+3)])
        i += 3
    return ll