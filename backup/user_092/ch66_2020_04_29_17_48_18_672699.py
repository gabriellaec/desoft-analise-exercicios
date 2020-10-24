def lista_sufixos(x):
    i = 0
    n = x
    L =[n]
    while i <= len(x):
        del L[n[0]]
        L.append(n)
        i += 1
    return(L)