def mais_populoso (d):
    li = []
    for i in d:
        s = 0
        for j in i.values():
            s += j
            li.append(s)
    a = max(li)
    b = li.index(a)
    k = 'a'
    for c in range(b):
        n = d.keys()
    return d