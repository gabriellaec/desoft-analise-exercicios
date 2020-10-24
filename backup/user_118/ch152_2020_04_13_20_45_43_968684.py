def verifica_preco(livro,dicionario_livros,dicionario_cores):
    if livro in dicionario_livros:
        cor_livro=dicionario_livros[livro]
        if cor_livro in dicionario_cores:
            valor=dicionario_cores[cor_livro]
            return valor