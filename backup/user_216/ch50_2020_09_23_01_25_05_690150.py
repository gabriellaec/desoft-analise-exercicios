def junta_nome_sobrenome(nomes,sobrenomes):
    e = ' '
    resposta = []
    i = 0
    while i < len(nomes):
        resposta.append(nomes[i] + e + sobrenomes[i])
        i += 1
    return resposta