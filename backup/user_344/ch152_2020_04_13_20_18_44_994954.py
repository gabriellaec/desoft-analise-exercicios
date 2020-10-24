def verifica_preco(titulo,dic_livros,cores):
    if titulo in dic_livros:
        cor = dic_livros[titulo]
        if cor in cores:
            preco = cores[cor]
    return preco
    
    