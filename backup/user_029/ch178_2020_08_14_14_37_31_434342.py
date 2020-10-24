def junta_nomes(a,b,c):
    listajuntas = []
    for i in a:
        if len(a) != 0:
            for d in c:
                listajuntas.append(i+''+d)
    for e in b:
        if len(b) != 0:
            for f in c:
                listajuntas.append(i+''+f)
    return listajuntas