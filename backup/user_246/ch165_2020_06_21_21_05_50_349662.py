def mais_populoso(p):
    total = 0
    for i in p:
        e = p[i]
        for t in e:
            total += e[t]
    return total
            