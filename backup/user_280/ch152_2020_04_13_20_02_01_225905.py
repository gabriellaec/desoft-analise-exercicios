def verifica_preco(titulo, dicionario_livros, tabela_cores):
    for titulo in dicionario_livros.keys():
        cor = dicionario_livros[titulo]
        for cor in tabela_cores.keys():
            preco = tabela_cores[cor]
    return preco
        