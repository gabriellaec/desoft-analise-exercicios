def verifica_preco(nome, lista_livros, lista_preco):
    if nome in lista_livros:
        cor = lista_livros[nome]
        if cor in lista_preco:
            preco = lista_preco[cor]
    return preco
    
    

    