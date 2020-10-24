def junta_nome_sobrenome(nomes, sobrenomes):
    
    nome_completo = list()
    
    for i in range(len(nomes)):
        nome_completo.append(nomes[i] + ' ' + sobrenomes[i])
    
    return nome_completo