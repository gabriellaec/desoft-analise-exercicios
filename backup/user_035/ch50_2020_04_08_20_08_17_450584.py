def junta_nome_sobrenome(ln, ls):
    i = 0
    while i<=len(ln):
        nome_completo = []
        nome_completo[i] = "{0} {1}".format(ln, ls)
        i += 1
    return nome_completo