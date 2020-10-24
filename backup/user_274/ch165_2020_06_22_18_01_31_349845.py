def mais_populoso(brasil):
    s = 0
    c = 0
    e = ""
    for a,i in brasil.items():
        for j in i.values():
            s = s+j
        if s > c:
            c = s
            e = i
    return e