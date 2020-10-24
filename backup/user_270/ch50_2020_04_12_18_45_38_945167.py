def junta_nome_sobrenome(ln,ls):
    l = []
    for i in range(len(ln-1)):
        l[i] = "{0} {1}".format(ln[i], ls[i])
    return l