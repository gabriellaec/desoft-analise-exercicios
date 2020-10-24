def calcula_media (l):
    li = []
    for i in l:
        for j in i.values():
            li.append(j)
    s = 0        
    for a in li:
        s += a
    return s/len(li)