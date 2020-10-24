def verifica_preco(livros,cores,titulo):
    for i in livros:
        if i == titulo:
            cor = livros[i]
            preco = cores[cor]
    return preco