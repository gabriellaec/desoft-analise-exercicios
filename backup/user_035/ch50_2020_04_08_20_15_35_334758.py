def junta_nome_sobrenome(ln, ls):
    nome_completo = []
    for i in range(len(ln)-1):
        nome_completo.append("{0} {1}".format(ln[i], ls[i]))
        i += 1
    print(nome_completo)