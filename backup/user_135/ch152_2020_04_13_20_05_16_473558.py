dicionario_livros = {"Pinóquio": "azul", "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
dicionario_cores = {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }

def verifica_preco(titulo_do_livro, args = dicionario_livros, dicionario_cores):
    
    titulo_do_livro = str(input())

    if titulo_do_livro in dicionario_livros:
        preco = dicionario_cores[dicionario_livros[titulo_do_livro]]
    else:
        print('Esse título não consta em nossa biblioteca.')
    
    return preco