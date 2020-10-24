def verifica_preco(titulo_do_livro, dicionario_de_livros, tabela_de_cores):
    if titulo_do_livro in dicionario_de_livros:
        return (tabela_de_cores[dicionario_de_livros[titulo_do_livro]])