def verifica_preco(livros,cores,titulo):
livros=dict()
cores=dict()
    for i in livros:
        if i == titulo:
            cor = livros[i]
            valor = cores[cor]
    return valor