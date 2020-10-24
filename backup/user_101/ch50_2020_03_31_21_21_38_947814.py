def junta_nome_sobrenome(nomes, sobrenomes):
    nome_completo = []
    i = 0
    while len(nome_completo) < len(nomes):
        nomeC = nomes[i] + ' ' + sobrenomes[i] 
        nome_completo.append(nomeC)
        i += 1
    return nome_completo