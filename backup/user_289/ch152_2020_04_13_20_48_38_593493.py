def verifica_preco(titulo, dict_nome_cor, dict_cor_preco):
    titulo_do_livro = str(titulo)
    
    for titulos,cores in dict_nome_cor.items():
        if titulo_do_livro == titulos:
            cor_do_livro = dict_nome_cor[titulos]
    
    for cores,precos in dict_cor_preco.items():
        if cor_do_livro == cores:
            preco_do_livro = dict_nome_cor[cores]
    
    return preco_do_livro