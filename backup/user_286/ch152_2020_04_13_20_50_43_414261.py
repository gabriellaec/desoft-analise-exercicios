def verifica_preco(titulo, dic_livro_cor, dic_cor_preco):

    for livro, cor in dic_livro_cor.items():
        if titulo == livro:
            for color, preco in dic_cor_preco.items():
                if cor == color:
                    return preco