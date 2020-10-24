def junta_nome_sobrenome(nomes, sobrenomes):
    completos = []
    i = 0
    while i < len(nome):
        junto = nome[i] + ' ' + sobrenome[i]
        completos.append(junto)
        i += 1
    return completos