def junta_nome_sobrenome(nome, sobrenome):
    nome_e_sobrenome = []
    i = 0
    while i < len(nome) and i < len(sobrenome):
        nome_e_sobrenome.append(nome[i] + ' ' + sobrenome[i])
        i += 1
    return nome_e_sobrenome