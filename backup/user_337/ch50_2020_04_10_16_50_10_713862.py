def junta_nome_sobrenome(nome,sobrenome):
    lista = []
    i = 0
    while i < len(nome):
        x = nome[i] + ' ' + sobrenome[i]
        lista.append(x)
        i += 1
    return lista
        