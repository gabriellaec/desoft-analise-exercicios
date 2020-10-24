def interseccao_chaves(D1,D2):
    chaves=[]
    chaves_final=[]
    for c in D1:
        chaves.append(c)
    for v in D2:
        if v in chaves:
            chaves_final.append(v)
        else:
            pass
    return chaves_final
    