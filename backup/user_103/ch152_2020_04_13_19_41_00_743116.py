def verifica_preco(livro,dicionario_livros,dicionario_cores):
    if livro in dicionario_livros:
        return dicionario_livros[livro]
    if dicionario_livros[livro] in dicionario_cores:
        print (dicionario_cores[dicionario_livros[livro]])
    
        