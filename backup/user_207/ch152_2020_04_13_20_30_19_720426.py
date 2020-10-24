def verifica_preco (titulo, dicionario_de_livros, dicionario_de_precos):
    #obs, o título é uma string
    if titulo in dicionario_de_livros:
        preco = dicionario_de_precos[dicionario_de_livros[titulo]]
    else:
        print ('O livro não consta na biblioteca')
    return preco