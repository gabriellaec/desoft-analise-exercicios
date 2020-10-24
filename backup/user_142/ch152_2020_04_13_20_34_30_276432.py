def verifica_preco (titulo, livro, preco):
    if titulo in livro:
        preco = livros[titulo]
        if preco in cor:
            cores = cor[preco]
    return cores
            

    