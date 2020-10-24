def junta_nome_sobrenome(nome, sobrenome):
    n = len(nome)
    i = 0
    e = ' '
    juntos = [0]*n
    while i < n:
        juntos[i] = nome[i] + e + sobrenome[i]
        i += 1
    return juntos