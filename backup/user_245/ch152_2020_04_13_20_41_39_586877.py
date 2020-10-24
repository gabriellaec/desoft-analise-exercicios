def verifica_preco(livro_escolhido,lista_de_livros,cor_p_precos):
    for livro_escolhido in lista_de_livros:
        livro = lista_de_livros[livro_escolhido]
        if cor_p_precos in lista_de_livros:
            preco = cor_p_precos[livro]
            return preco