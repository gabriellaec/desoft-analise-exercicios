def junta_nome_sobrenome(nome, sobrenome):
    resposta = []
    i = 0
    while len(nome) == len(sobrenome):
        nome_completo = nome[i] + sobrenome[i]
        resposta.append(nome_completo)
    return resposta