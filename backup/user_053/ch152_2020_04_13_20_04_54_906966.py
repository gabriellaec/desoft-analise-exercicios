def verifica_preco(titulo_livro, dict_nome_cor, dict_cores_valores):
    # Localiza livro e sua respectiva cor
    for nome, cor in dict_nome_cor.items():
        if nome == titulo_livro:
            cor_associada = cor
    # Localiza preço referente à cor anterior encontrada
    for cores, valores in dict_cores_valores.items():
        if cores == cor_associada:
            preco = valores
    return preco