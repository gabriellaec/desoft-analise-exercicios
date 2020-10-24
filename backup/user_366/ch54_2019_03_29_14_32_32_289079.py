def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    new = [0]*len(nome)
    while i < len(nome):
        new[i] = ('{0} {1}'. format(nome[i], sobrenome[i]))
        i += 1
    return new