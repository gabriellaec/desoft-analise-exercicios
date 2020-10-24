def junta_nome_sobrenome(nome, sobrenome):
    resposta = []
    nome_completo = 0
    i = 0
    while len(nome) == len(sobrenome):
        nome_completo[i] = nome[i] + sobrenome[i]
        resposta.append(nome_completo)
        i = i + 1
    return resposta