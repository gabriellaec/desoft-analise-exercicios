def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    while i < len(nome):
        nome_completo = nome[i] + sobrenome[i]
        nova_lista.append(nome_completo)
        i += 1
    return nova_lista
    