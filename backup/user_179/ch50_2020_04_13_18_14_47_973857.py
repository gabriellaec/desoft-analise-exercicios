def junta_nome_sobrenome (nome,sobrenome):
    lista = []
    i = 0
    while i < len(nome):
        lista.append(nome[i]+sobrenome[i])
        i = i + 1
    return lista