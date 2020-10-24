def verifica_progressao(lista):
    r = []
    q = []
    pa = False
    pg = False
    for i,e in enumerate(lista):
        razaopa = lista[-1]-lista[-2]
        razaopg = lista[-1]/lista[-2]
        del lista[-1]
        r.append(razaopa)
        q.append(razaopg)
    for f in range(1,len(r)):
        if not pa and r[f] != r[-f]:
            pa = False
        elif pa or r[f] == r[-f]:
            pa = True
    for g in range(1,len(q)):
        if not pg and q[f] != q[-f]:
            pg = False
        elif pg or q[f] == q[-f]:
            pg = True
    if pa and pg:
        return AG
    elif pa:
        return PA
    elif pg:
        return PG
    else:
        return NA