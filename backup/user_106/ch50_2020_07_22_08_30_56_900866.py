def junta_nome_sobrenome(nomes, sobrenomes):
    completos = []
    i = 0
    while i < len(nomes):
        junto = nomes[i] + ' ' + sobrenomes[i]
        completos.append(junto)
        i += 1
    return completos