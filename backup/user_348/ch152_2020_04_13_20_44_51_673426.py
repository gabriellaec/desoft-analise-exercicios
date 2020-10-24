def verifica_preco (titulo, dicionario_livros, tabela_cores):
    i =0
    while i < len(dicionario_livros):
        if i == titulo:
            cor = dicionario_livros[i]
        i = i + 1
    t = 0
    while t < len(tabela_cores):
        if t == cor:
            preço = tabela_cores[t]
        t = t +1
    return preço
    