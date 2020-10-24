def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    nome_sobrenome = []
    while i < len(nome):
        nome_sobrenome.append(nome[i] + ' ' + sobrenome[i])
        i += 1
    return nome_sobrenome