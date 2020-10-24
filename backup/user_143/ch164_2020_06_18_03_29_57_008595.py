def traduz (l, d):
    li = []
    c = 0
    for j, i in d.items():
        if l[c] == j:
            li.append(i)
            c +=1
    return li