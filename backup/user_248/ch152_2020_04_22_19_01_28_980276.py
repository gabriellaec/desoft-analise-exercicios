def verifica_preco(titulo, livros, cores):
    cor=''
    preco=0
    if titulo in livros:
        cor=livros[titulo]
        if cor in cores:
            preco=cores[cor]
    return preco
            
           