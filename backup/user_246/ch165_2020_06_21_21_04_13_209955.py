def mais_populoso(p):
    total = 0
    for i in p:
        e = i
        for t in i:
            total += e[t]
    return total
            