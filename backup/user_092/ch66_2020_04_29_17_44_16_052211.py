def lista_sufixos(x):
    i = 0
    L =[]
    n = x
    while i <= len(x):
        L.append(n)
        del n[0]
        i += 1
    print(L)