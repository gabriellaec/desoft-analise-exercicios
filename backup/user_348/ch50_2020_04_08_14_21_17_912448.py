def junta_nome_sobrenome(nome, sobrenome):
    resposta = []
    i = 0
    while len(nome) == len(sobrenome):
        resposta = nome + sobrenome
        resposta.append(i)
    return resposta