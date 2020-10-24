def junta_nome_sobrenome(ln,ls):
    l = [0]*len(ls)
    i = 0
    while i < len(ln):
        l[i] = "{0} {1}".format(ln[i], ls[i])
        i += 1
    return l