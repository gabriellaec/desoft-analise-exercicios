def junta_nome_sobrenome(nomes, sobrenomes):
    lista_nome_sobrenome = []
    for i in range(len(nomes)):
        lista_nome_sobrenome.append(nomes[i] + ' ' + sobrenomes[i])
    return lista_nome_sobrenome