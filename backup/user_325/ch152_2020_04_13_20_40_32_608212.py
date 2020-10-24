def verifica_preco(nome,dic_livro,dic_cor):
    if nome in dic_livro:
        cor = dic_livro[nome]
        if cor in dic_cor:
            preco = dic_cor[cor]
            return preco