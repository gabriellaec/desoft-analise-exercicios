def junta_nome_sobrenome(nomes, sobrenomes):
    nome_sobrenome = []
    i = 0
    while i < len(nomes):
        nome_final = '{0} {1}' .format(nomes[i], sobrenomes[i])
        nome_sobrenome.append(nome_final)
        i += 1    
    return nome_sobrenome