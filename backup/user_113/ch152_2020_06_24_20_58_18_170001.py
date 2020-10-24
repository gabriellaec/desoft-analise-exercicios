def verifica_preco(livro, catalogo, cores):
    if livro in catalogo:
        catalogo[livro] = cores[livro]
        preco = cores[catalogo]
    return preco