def verifica_preco (titulo, livro, preco):
    if titulo in livro:
        precos = livro[titulo]
    if precos in preco:
        valor = preco[precos]
    return valor
            

    