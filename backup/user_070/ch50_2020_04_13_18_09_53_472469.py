def junta_nome_sobrenome(nome, sobrenome):
    n = len(nome)
    i = 0
    e = ' '
    juntos = []
    while i < n:
        juntos.append(nome[i] + e + sobrenome[i])
        i += 1
    return juntos