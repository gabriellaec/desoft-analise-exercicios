def verifica_preco(titulo,dic_livro,dic_cor):
    if titulo in dic_livro:
        cor = dic_livro[titulo]
        if cor in dic_cor:
            preco = dic_cor[cor]
            return preco