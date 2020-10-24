def junta_nome_sobrenome(nome, sobrenome):
    l2 = []
    i = 0
    while i<len(nome):
        l2.append(' '.join(nome[i], sobrenome[i]))
        i += 1
    return l2
                  