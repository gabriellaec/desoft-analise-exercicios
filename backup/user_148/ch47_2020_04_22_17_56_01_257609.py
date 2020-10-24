def estritamente_crescente(l):
    l2 = []
    if len(l) == 0:
        return l2
    crescente = True
    i = 1
    while i<len(l):
        if l[i-1] >= l[i]:
            crescente = False
        else:
            l2.append(l[i-1])
    return l2
