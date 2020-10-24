def verifica_preco(titulo, dicionario_livros, tabela_cores):
    for livro in dicionario_livros.keys():
        if livro == titulo:
            cor = dicionario_livros[titulo]
            preco = tabela_cores[cor]
    return preco
        