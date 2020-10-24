def verifica_preco(nome,cor,livro):
    for nome in livro:
        cor_livro = livro[nome]
        if cor_livro in cor:
            preco=cor[cor_livro]
            return preco