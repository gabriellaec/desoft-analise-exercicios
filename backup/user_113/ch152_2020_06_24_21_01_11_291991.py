def verifica_preco(livro, catalogo, cores):
    if livro in catalogo:
        cor = catalogo[livro]
        preco = cores[cor]
    return preco