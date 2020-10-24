def junta_nome_sobrenome(ln, ls):
    for i in range len(ln)-1:
        nome_completo = []*len(ln)
        nome_completo[i] = "{0} {1}".format(ln, ls)
        i += 1
    return nome_completo