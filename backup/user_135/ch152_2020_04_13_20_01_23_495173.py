dicionario_livros = input({})
dicionario_cores = input({})

def verifica_preco(titulo_do_livro):
    
    titulo_do_livro = str(input())

    if titulo_do_livro in dicionario_livros:
        cor = dicionario_livros[titulo_do_livro]
    else:
        print('Esse título não consta em nossa biblioteca.')
        
    preco = dicionario_cores[cor]
    return preco