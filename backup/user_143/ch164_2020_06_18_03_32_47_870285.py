def traduz (l, d):
    li = []
    c = 0
    a = 0
    while a < len(l):
        for j, i in d.items():
            if l[c] == j:
                li.append(i)
        a +=1
        c +=1
    return li