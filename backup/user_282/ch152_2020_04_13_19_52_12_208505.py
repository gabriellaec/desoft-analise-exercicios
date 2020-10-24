def verifica_preco(titulo, livros, cores):
    if titulo in livros:
        cor = livros[titulo]
        if cor in cores:
            preco = cores[cor]
    return preco