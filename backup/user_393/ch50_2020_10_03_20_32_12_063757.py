def junta_nome_sobrenome(nomes, sobrenomes):
    nome_e_sobrenome= []
    i= 0
    while i < len(nomes):
        nome_e_sobrenome.append("{0} {1}".format(nomes[i], sobrenomes[i]))
        i= i + 1
    return nome_e_sobrenome