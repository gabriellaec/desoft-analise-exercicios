def verifica_preco(escolha,lista_de_livros,cor_p_precos):
    if escolha in lista_de_livros:
        livro = lista_de_livros[escolha]
        if livro in cor_p_precos:
            preco = cor_p_precos[livro]
            return preco