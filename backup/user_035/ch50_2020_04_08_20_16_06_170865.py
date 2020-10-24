def junta_nome_sobrenome(ln, ls):
    nome_completo = []
    for i in range(len(ln)):
        nome_completo.append("{0} {1}".format(ln[i], ls[i]))
        i += 1
    return nome_completo