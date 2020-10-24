def junta_nomes(a,b,c):
    listajunta = []
    for i in a:
        if len(a) > 0:
            for d in c:
                listajunta.append(i+''+d)
    for e in b:
        if len(b) > 0:
            for f in c:
                listajunta.append(i+''+f)
    return listajunta