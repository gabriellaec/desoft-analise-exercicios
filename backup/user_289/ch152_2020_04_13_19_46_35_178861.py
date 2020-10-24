def verifica_preco(titulo, dict_nome_cor, dict_cor_preco):
    titulo_do_livro = str(titulo)
    
    for titulos in dict_nome_cor.keys():
        if titulo_do_livro == titulos:
            cor_do_livro = dict_nome_cor[titulos]
    
    for cores in dict_cor_preco.keys():
        if cor_do_livro == cores:
            preco_do_livro = dict_nome_cor[cores]
    
    return preco_do_livro