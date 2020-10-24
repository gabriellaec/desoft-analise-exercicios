def junta_nomes(a,b,c):
    lis = []
    for i in a:
        if len(a) != 0:
            for d in c:
                lis.append(i+''+d)
    for e in b:
        if len(b) != 0:
            for f in c:
                lis.append(i+''+f)
    return lis