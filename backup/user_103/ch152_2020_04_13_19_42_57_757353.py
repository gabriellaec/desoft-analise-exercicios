def verifica_preco(livro,dicionario_livros,dicionario_cores):
    if livro in dicionario_livros:
        cor=dicionario_livros[livro]
    if cor in dicionario_cores:
        return dicionario_cores[cor]
    
        