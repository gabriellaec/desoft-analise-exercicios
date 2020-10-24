def junta_nome_sobrenome(nomes, sobrenomes):
    nome_completo = []
    i = 0
    while len(nome_completo) < len(nomes):
        nome_completo[i] = nomes[i] + ' ' + sobrenomes[i] 
        i += 1
    return nome_completo