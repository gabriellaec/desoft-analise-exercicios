def junta_nome_sobrenome(nome, sobrenome):
    i = 0
    e = ' '
    juntos = []
    for n in nome:
        juntos.append(n + e + sobrenome[i])
        i += 1
    return juntos