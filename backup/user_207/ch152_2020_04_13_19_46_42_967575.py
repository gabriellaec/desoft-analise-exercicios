def verifica_preco (titulo, dicionario_de_livros, dicionario_de_precos):
    
    if titulo in dicionario_de_livros:
        preco = dicionario_de_precos[dicionario_de_livros[titulo]]
    return preco