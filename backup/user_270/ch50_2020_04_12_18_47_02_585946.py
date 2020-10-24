def junta_nome_sobrenome(ln,ls):
    l = []
    i = 0
    while i < range(len(ln)-1):
        l[i] = "{0} {1}".format(ln[i], ls[i])
        i += 1
    return l