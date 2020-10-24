def junta_nome_sobrenome(nomes,sobrenomes):
    resposta = [] * len(nomes)
    i = 0
    while i < len(nomes):
        resposta[i] = "{0} {1}".format(nomes[i], sobrenomes[i])
        i += 1
    return resposta