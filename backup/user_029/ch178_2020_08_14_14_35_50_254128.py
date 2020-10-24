def junta_nomes(a,b,c):
    listajunta = []
    i = 0
    e = 0
    while i in len(a):
        if len(a) != 0:
            for d in c:
                listajunta.append(i+''+d)
                i+=1
    while i in len(b):
        if len(b) != 0:
            for f in c:
                listajunta.append(i+''+f)
                e+=1
    return listajunta