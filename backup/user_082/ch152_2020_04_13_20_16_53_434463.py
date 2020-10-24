def verifica_preco(titulo_livro, dic_livro_cor, preco_cor):
    checagem_cor= dic_livro_cor.get(titulo_livro)
    preco= preco_cor.get(checagem_cor)
    return preco
