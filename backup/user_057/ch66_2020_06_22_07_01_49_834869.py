def lista_sufixos(str):
    suf = []
    T = len(str)
    i = 0
    while i > T:
        suf = suf.append(str[i:T])
        i +=1
    return suf