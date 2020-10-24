def verifica_preco(nome, cor,livro):
    if nome in livro:
        cor_livro = livro[nome]
        if cor_livro in cor:
            preco=cor[cor_livro]
            return preco