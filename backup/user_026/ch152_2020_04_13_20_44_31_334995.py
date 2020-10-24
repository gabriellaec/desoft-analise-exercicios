def verifica_preco (string, livros, precos):

    if string in livros:
        cor = livros[string]
    if cor in precos:
        total = precos[cor]
        return total