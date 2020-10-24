def verifica_preco (titulo, dicionario_livros, tabela_cores):
    for i in dicionario_livros:
        if i == titulo:
            cor = dicionario_livros[i]
    for c in tabela_cores:
        if c ==cor:
            preço = tabela_cores[c]
    return preço
    