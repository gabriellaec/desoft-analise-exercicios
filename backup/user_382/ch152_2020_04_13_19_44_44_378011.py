def verifica_preco(titulo, dic_nomes, dic_precos):
    for i in dic_nomes:
        if i == titulo:
            cor = dic_nomes[i]
            preco = dic_precos[cor]
    return preco 