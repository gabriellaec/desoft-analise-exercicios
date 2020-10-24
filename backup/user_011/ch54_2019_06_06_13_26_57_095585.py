def junta_nome_sobrenome(nome, sobrenome):
    nome_sobrenome = []
    i = 0
    while i < len(nome):
        a = ' '.join(nome[i], sobrenome[i])
        nome_sobrenome.append(a)
        i += 1
    return nome_sobrenome
