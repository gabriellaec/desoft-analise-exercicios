def verifica_preco(titulo, dict_nome_cor, dict_cor_preco):
    titulo_do_livro = str(titulo)
    cor_do_livro = dict_nome_cor[titulo_do_livro]
    preco_do_livro = dict_nome_cor[cor_do_livro]
    return preco_do_livro