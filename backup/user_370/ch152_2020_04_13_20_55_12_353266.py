def verifica_preco (titulo_livro,dicionario_livro,dicionario_preco):
    cores= dicionario_livro[titulo_livro]
    preco=dicionario_preco[cores]
    return preco