def verifica_preco(titulo, dict_nome_cor, dict_cor_preco):
    titulo_do_livro = str(titulo)
    if titulo_do_livro in dict_nome_cor.keys():
        cor_do_livro = dict_nome_cor[titulo_do_livro]
        if cor_do_livro in dict_cor_preco.keys():
            return dict_nome_cor[cor_do_livro]