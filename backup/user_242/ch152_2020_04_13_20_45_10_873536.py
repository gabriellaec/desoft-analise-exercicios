def verifica_preco(titulo_do_livro, dicionario_livro, tabela_de_cores):
    if titulo_do_livro in dicionario_livro:
        cor = dicionario_livro[titulo_do_livro]
        if cor in tabela_de_cores:
            preco = tabela_de_cores[cor]
            return preco