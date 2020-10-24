def verifica_preco(livro, catalogo, cores):
    if livro in catalogo:
        catalogo[livro] = cores[catalogo]
        preco = cores[catalogo]
    return preco