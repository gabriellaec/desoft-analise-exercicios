def mais_populoso(p):
    total = 0
    for i in p:
        for t in i:
            total += i[t]
    return total
            