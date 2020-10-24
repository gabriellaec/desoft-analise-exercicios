def verifica_preco(nome,livro,cor):
    if nome in livro:
        cor_livro = livro[nome]
        if cor_livro in cor:
            preco=cor[cor_livro]
            return preco