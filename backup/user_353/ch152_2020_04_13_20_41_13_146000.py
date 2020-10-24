def verifica_preco(titulo, dict_nome_cor, dict_cor_preco):
 
    if tit_livro in dict_nome_cor.keys():
        cor_livro = dict_nome_cor[tit_livro]
        if cor_livro in dict_cor_preco.keys():
            preço_livro = dict_nome_cor[cor_livro]
        return preço_livro