def junta_nome_sobrenome (nomes, sobrenomes):
    nome_sobrenome = []
    for i in range (len(nomes)):
        nome_sobrenome.append(nomes[i]+" "+sobrenomes[i])
    return nome_sobrenome