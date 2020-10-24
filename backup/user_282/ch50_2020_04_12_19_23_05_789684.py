def junta_nome_sobrenome(nome, sobrenome):
    lista = list()
    for i in range(len(nome)):
        a = '{0} {1}'.format(nome[i], sobrenome[i])
        lista.append(a)
    return lista